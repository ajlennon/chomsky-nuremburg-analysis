"""
Nuremberg Trials Document Scraper

Scrapes and indexes documents from the Harvard Law School Library's
Nuremberg Trials Project website.

Copyright (C) 2025
License: GPL-3.0-or-later
"""

import logging
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set
from urllib.parse import urljoin, urlparse

import requests
import requests.compat
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


@dataclass
class Document:
    """Represents a document from the Nuremberg Trials Project"""

    url: str
    title: str
    trial: str
    document_type: str
    text_content: Optional[str] = None
    metadata: Optional[Dict] = None
    page_images: Optional[List[str]] = None


class NurembergDocumentScraper:
    """Scraper for Harvard Nuremberg Trials Project documents"""

    BASE_URL = "https://nuremberg.law.harvard.edu/"

    def __init__(self, cache_dir: Optional[Path] = None, rate_limit: float = 1.0):
        """
        Initialize scraper

        Args:
            cache_dir: Directory to cache downloaded documents
            rate_limit: Seconds to wait between requests
        """
        self.cache_dir = cache_dir or Path("./nuremberg_cache")
        self.cache_dir.mkdir(exist_ok=True, parents=True)
        self.rate_limit = rate_limit
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (compatible; NurembergAnalysis/1.0; +https://github.com/ajlennon/nuremberg-analysis)"
            }
        )
        self.documents: List[Document] = []
        self.visited_urls: Set[str] = set()

    def _make_request(self, url: str, retries: int = 3) -> Optional[requests.Response]:
        """Make HTTP request with retries and rate limiting"""
        if url in self.visited_urls:
            return None

        for attempt in range(retries):
            try:
                time.sleep(self.rate_limit)
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                self.visited_urls.add(url)
                return response
            except requests.RequestException as e:
                log.warning(f"Request failed (attempt {attempt + 1}/{retries}): {url} - {e}")
                if attempt < retries - 1:
                    time.sleep(2**attempt)  # Exponential backoff
                else:
                    log.error(f"Failed to fetch {url} after {retries} attempts")
                    return None
        return None

    def _parse_document_page(self, url: str, html: str) -> Optional[Document]:
        """Parse a document page and extract metadata"""
        soup = BeautifulSoup(html, "html.parser")

        # Extract title
        title_elem = soup.find("title") or soup.find("h1")
        title = title_elem.get_text(strip=True) if title_elem else "Untitled"

        # Try to determine trial and document type from URL or content
        trial = self._extract_trial_from_url(url)
        doc_type = self._extract_doc_type_from_url(url)

        # Extract text content
        text_content = self._extract_text_content(soup)

        # Extract metadata
        metadata = self._extract_metadata(soup)

        # Extract page image links
        page_images = self._extract_page_images(soup)

        return Document(
            url=url,
            title=title,
            trial=trial,
            document_type=doc_type,
            text_content=text_content,
            metadata=metadata,
            page_images=page_images,
        )

    def _extract_trial_from_url(self, url: str) -> str:
        """Extract trial name from URL"""
        url_lower = url.lower()
        if "imt" in url_lower or "international-military-tribunal" in url_lower:
            return "IMT"
        if "nmt" in url_lower:
            # Extract NMT number if present
            match = re.search(r"nmt[_\s-]?(\d+)", url_lower)
            if match:
                return f"NMT {match.group(1)}"
            return "NMT"
        if "tokyo" in url_lower or "imtfe" in url_lower:
            return "Tokyo (IMTFE)"
        return "Unknown"

    def _extract_doc_type_from_url(self, url: str) -> str:
        """Extract document type from URL"""
        url_lower = url.lower()
        if "transcript" in url_lower:
            return "Transcript"
        if "document" in url_lower or "exhibit" in url_lower:
            return "Document/Exhibit"
        if "brief" in url_lower:
            return "Brief"
        if "judgment" in url_lower or "verdict" in url_lower:
            return "Judgment"
        if "dissent" in url_lower:
            return "Dissent"
        if "photograph" in url_lower or "photo" in url_lower:
            return "Photograph"
        return "Unknown"

    def _extract_text_content(self, soup: BeautifulSoup) -> str:
        """Extract main text content from page"""
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        # Try to find main content area
        main_content = (
            soup.find("main")
            or soup.find("article")
            or soup.find("div", class_=re.compile("content|main|text"))
        )

        if main_content:
            text = main_content.get_text(separator="\n", strip=True)
        else:
            text = soup.get_text(separator="\n", strip=True)

        # Clean up excessive whitespace
        text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
        return text.strip()

    def _extract_metadata(self, soup: BeautifulSoup) -> Dict:
        """Extract metadata from page"""
        metadata = {}

        # Look for metadata in meta tags
        for meta in soup.find_all("meta"):
            name = meta.get("name") or meta.get("property")
            content = meta.get("content")
            if name and content:
                metadata[name] = content

        # Look for structured data
        # Add more metadata extraction as needed

        return metadata

    def _extract_page_images(self, soup: BeautifulSoup) -> List[str]:
        """Extract links to page images"""
        images = []
        for img in soup.find_all("img"):
            src = img.get("src")
            if src:
                full_url = urljoin(self.BASE_URL, src)
                images.append(full_url)
        return images

    def search_documents(
        self, query: str, trial: Optional[str] = None, doc_type: Optional[str] = None
    ) -> List[Document]:
        """
        Search for documents using the website's search functionality

        Args:
            query: Search query
            trial: Filter by trial (e.g., "IMT", "Tokyo", "NMT 1")
            doc_type: Filter by document type

        Returns:
            List of matching documents
        """
        # The website has a search interface - we'll need to use it
        search_url = urljoin(self.BASE_URL, "search")

        # Build search parameters
        from urllib.parse import urlencode

        params = {
            "q": query,
            "include_images": "true",
            "include_documents": "true",
            "include_transcripts": "true",
            "include_photographs": "true",
        }

        response = self._make_request(f"{search_url}?{urlencode(params)}")
        if not response:
            return []

        # Parse search results
        soup = BeautifulSoup(response.text, "html.parser")
        results = []

        # Find result links (structure depends on website)
        for link in soup.find_all("a", href=True):
            href = link.get("href")
            if href and ("document" in href.lower() or "transcript" in href.lower()):
                full_url = urljoin(self.BASE_URL, href)
                doc = self.fetch_document(full_url)
                if doc:
                    # Apply filters
                    if trial and doc.trial != trial:
                        continue
                    if doc_type and doc.document_type != doc_type:
                        continue
                    results.append(doc)

        return results

    def fetch_document(self, url: str) -> Optional[Document]:
        """Fetch and parse a single document"""
        # Check cache first
        cache_file = self.cache_dir / self._url_to_filename(url)
        if cache_file.exists():
            log.info(f"Loading from cache: {url}")
            with open(cache_file, encoding="utf-8") as f:
                # For now, re-fetch to get fresh data
                # Could implement proper caching later
                pass

        response = self._make_request(url)
        if not response:
            return None

        doc = self._parse_document_page(url, response.text)
        if doc:
            self.documents.append(doc)
            # Cache the document
            self._cache_document(doc)

        return doc

    def _url_to_filename(self, url: str) -> str:
        """Convert URL to safe filename"""
        parsed = urlparse(url)
        path = parsed.path.strip("/").replace("/", "_")
        # Remove query params for filename
        return re.sub(r"[^\w\-_.]", "_", path) + ".html"

    def _cache_document(self, doc: Document):
        """Cache document to disk"""
        cache_file = self.cache_dir / self._url_to_filename(doc.url)
        with open(cache_file, "w", encoding="utf-8") as f:
            f.write(f"URL: {doc.url}\n")
            f.write(f"Title: {doc.title}\n")
            f.write(f"Trial: {doc.trial}\n")
            f.write(f"Type: {doc.document_type}\n")
            f.write("\n--- Content ---\n\n")
            if doc.text_content:
                f.write(doc.text_content)

    def find_pal_dissent(self) -> List[Document]:
        """Search specifically for Justice Pal's dissent"""
        queries = [
            "Radhabinod Pal dissent",
            "Pal dissent Tokyo",
            "Pal judgment dissent",
            "Indian justice Pal Tokyo",
        ]

        results = []
        for query in queries:
            docs = self.search_documents(query, trial="Tokyo (IMTFE)")
            results.extend(docs)

        # Remove duplicates
        seen_urls = set()
        unique_results = []
        for doc in results:
            if doc.url not in seen_urls:
                seen_urls.add(doc.url)
                unique_results.append(doc)

        return unique_results

    def find_yamashita_documents(self) -> List[Document]:
        """Search for documents related to General Yamashita"""
        queries = ["Yamashita", "Yamashita Philippines", "Yamashita judgment", "Yamashita trial"]

        results = []
        for query in queries:
            docs = self.search_documents(query, trial="Tokyo (IMTFE)")
            results.extend(docs)

        # Remove duplicates
        seen_urls = set()
        unique_results = []
        for doc in results:
            if doc.url not in seen_urls:
                seen_urls.add(doc.url)
                unique_results.append(doc)

        return unique_results

    def find_telford_taylor_documents(self) -> List[Document]:
        """Search for documents related to Telford Taylor"""
        queries = ["Telford Taylor", "Taylor prosecutor", "Taylor Nuremberg"]

        results = []
        for query in queries:
            docs = self.search_documents(query)
            results.extend(docs)

        # Remove duplicates
        seen_urls = set()
        unique_results = []
        for doc in results:
            if doc.url not in seen_urls:
                seen_urls.add(doc.url)
                unique_results.append(doc)

        return unique_results

    def find_bombing_documents(self) -> List[Document]:
        """Search for documents discussing bombing of cities"""
        queries = [
            "bombing cities",
            "Dresden",
            "Tokyo bombing",
            "urban bombing",
            "atomic bomb",
            "atom bomb",
        ]

        results = []
        for query in queries:
            docs = self.search_documents(query)
            results.extend(docs)

        # Remove duplicates
        seen_urls = set()
        unique_results = []
        for doc in results:
            if doc.url not in seen_urls:
                seen_urls.add(doc.url)
                unique_results.append(doc)

        return unique_results
