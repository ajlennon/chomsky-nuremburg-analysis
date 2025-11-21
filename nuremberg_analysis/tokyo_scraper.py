"""
Tokyo Trials Document Scraper

Scrapes and indexes documents from Tokyo Trials archives including:
- Tokyo Trial Database (tokyotrial.cn)
- University of Wisconsin-Madison Libraries
- Japan Center for Asian Historical Records (JACAR)
- Hoover Institution Library & Archives

Copyright (C) 2025
License: GPL-3.0-or-later
"""

import logging
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


@dataclass
class TokyoDocument:
    """Represents a document from Tokyo Trials archives"""

    url: str
    title: str
    source: str  # "tokyotrial.cn", "wisconsin", "jacar", "hoover"
    document_type: str
    text_content: Optional[str] = None
    metadata: Optional[Dict] = None
    page_images: Optional[List[str]] = None
    volume: Optional[str] = None
    page_numbers: Optional[List[int]] = None


class TokyoDocumentScraper:
    """Scraper for Tokyo Trials documents from multiple sources"""

    # Base URLs for different archives
    TOKYO_TRIAL_DB_URL = "http://tokyotrial.cn"
    WISCONSIN_URL = "https://digital.library.wisc.edu/1711.web/tokyo-trials"
    JACAR_URL = "https://www.jacar.go.jp/english/"
    HOOVER_URL = "https://oac.cdlib.org/findaid/ark:/13030/kt6b69q2rf"

    def __init__(self, cache_dir: Optional[Path] = None, rate_limit: float = 2.0):
        """
        Initialize scraper

        Args:
            cache_dir: Directory to cache downloaded documents
            rate_limit: Seconds to wait between requests
        """
        self.cache_dir = cache_dir or Path("./tokyo_cache")
        self.cache_dir.mkdir(exist_ok=True, parents=True)
        self.rate_limit = rate_limit
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (compatible; TokyoTrialsAnalysis/1.0; +https://github.com/ajlennon/chomsky-nuremburg-analysis)"
            }
        )
        self.documents: List[TokyoDocument] = []
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

    def search_tokyo_trial_db(self, query: str, max_results: int = 50) -> List[TokyoDocument]:
        """
        Search the Tokyo Trial Database (tokyotrial.cn)
        
        Note: This database may require login or have access restrictions
        """
        log.info(f"Searching Tokyo Trial Database for: {query}")
        documents = []
        
        # Try to search - note: may require login
        search_url = f"{self.TOKYO_TRIAL_DB_URL}/Resource"
        params = {"sn": query}
        
        try:
            response = self._make_request(search_url, params=params)
            if response:
                soup = BeautifulSoup(response.text, "html.parser")
                # Parse search results
                # Implementation depends on actual site structure
                log.info(f"Found results on Tokyo Trial Database")
        except Exception as e:
            log.warning(f"Could not search Tokyo Trial Database: {e}")
        
        return documents

    def search_pal_dissent(self) -> List[TokyoDocument]:
        """Search for Pal's dissent document"""
        log.info("Searching for Pal's dissent document")
        documents = []
        
        # Pal's profile page on Tokyo Trial Database
        pal_url = f"{self.TOKYO_TRIAL_DB_URL}/Person/Index/7cf1a279c0964d1cad5f160f69768cf8"
        
        try:
            response = self._make_request(pal_url)
            if response:
                soup = BeautifulSoup(response.text, "html.parser")
                
                # Extract Pal's profile information
                profile_text = self._extract_text_content(soup)
                
                # Create document from profile page
                profile_doc = TokyoDocument(
                    url=pal_url,
                    title="Pal, Radha Binod - Judge Profile",
                    source="tokyotrial.cn",
                    document_type="Profile",
                    text_content=profile_text,
                    metadata={"related_to": "Pal profile"}
                )
                documents.append(profile_doc)
                
                # Look for references to Pal's dissent
                # The page mentions books about Pal's dissent
                book_links = soup.find_all("a", href=re.compile(r"/Book/index/"))
                for link in book_links:
                    book_url = urljoin(self.TOKYO_TRIAL_DB_URL, link.get("href", ""))
                    title = link.get_text(strip=True)
                    
                    if "帕尔" in title or "Pal" in title or "dissent" in title.lower() or "异议" in title:
                        # Try to fetch book page content
                        try:
                            book_response = self._make_request(book_url)
                            book_text = ""
                            if book_response:
                                book_soup = BeautifulSoup(book_response.text, "html.parser")
                                book_text = self._extract_text_content(book_soup)
                        except:
                            book_text = ""
                        
                        doc = TokyoDocument(
                            url=book_url,
                            title=title,
                            source="tokyotrial.cn",
                            document_type="Book/Research Material",
                            text_content=book_text,
                            metadata={"related_to": "Pal dissent"}
                        )
                        documents.append(doc)
                        log.info(f"Found Pal-related document: {title}")
        except Exception as e:
            log.warning(f"Could not fetch Pal profile: {e}")
        
        return documents

    def search_yamashita(self) -> List[TokyoDocument]:
        """Search for Yamashita case documents"""
        log.info("Searching for Yamashita case documents")
        documents = []
        
        # Note: Yamashita was tried separately, not at Tokyo Trials
        # But may be referenced in Tokyo Trial documents
        # Search Tokyo Trial Database
        search_url = f"{self.TOKYO_TRIAL_DB_URL}/Resource?sn=Yamashita"
        
        try:
            response = self._make_request(search_url)
            if response:
                soup = BeautifulSoup(response.text, "html.parser")
                # Parse results
                log.info("Searching for Yamashita references")
        except Exception as e:
            log.warning(f"Could not search for Yamashita: {e}")
        
        return documents

    def search_trial_transcripts(self, keywords: List[str], max_results: int = 100) -> List[TokyoDocument]:
        """Search trial transcripts for keywords"""
        log.info(f"Searching trial transcripts for: {keywords}")
        documents = []
        
        # Search Tokyo Trial Database court records
        court_records_url = f"{self.TOKYO_TRIAL_DB_URL}/Resource?type=9"  # Court records type
        
        try:
            response = self._make_request(court_records_url)
            if response:
                soup = BeautifulSoup(response.text, "html.parser")
                # Parse court record listings
                # Look for links to transcripts
                transcript_links = soup.find_all("a", href=re.compile(r"xmlread|PdfEvdRead"))
                
                for link in transcript_links[:max_results]:
                    transcript_url = urljoin(self.TOKYO_TRIAL_DB_URL, link.get("href", ""))
                    title = link.get_text(strip=True)
                    
                    # Try to fetch transcript content
                    try:
                        transcript_response = self._make_request(transcript_url)
                        transcript_text = ""
                        if transcript_response:
                            transcript_soup = BeautifulSoup(transcript_response.text, "html.parser")
                            transcript_text = self._extract_text_content(transcript_soup)
                    except Exception as e:
                        log.debug(f"Could not fetch transcript content: {e}")
                        transcript_text = ""
                    
                    doc = TokyoDocument(
                        url=transcript_url,
                        title=title,
                        source="tokyotrial.cn",
                        document_type="Trial Transcript",
                        text_content=transcript_text,
                        metadata={"keywords": keywords}
                    )
                    documents.append(doc)
        except Exception as e:
            log.warning(f"Could not search trial transcripts: {e}")
        
        return documents

    def _parse_document_page(self, url: str, html: str, source: str) -> Optional[TokyoDocument]:
        """Parse a document page and extract metadata"""
        soup = BeautifulSoup(html, "html.parser")
        
        # Extract title
        title_elem = soup.find("title") or soup.find("h1")
        title = title_elem.get_text(strip=True) if title_elem else "Untitled"
        
        # Extract document type
        doc_type = self._extract_doc_type_from_url(url)
        
        # Extract text content
        text_content = self._extract_text_content(soup)
        
        # Extract metadata
        metadata = self._extract_metadata(soup)
        
        # Extract volume and page numbers if present
        volume, page_numbers = self._extract_volume_pages(soup, url)
        
        return TokyoDocument(
            url=url,
            title=title,
            source=source,
            document_type=doc_type,
            text_content=text_content,
            metadata=metadata,
            volume=volume,
            page_numbers=page_numbers,
        )

    def _extract_doc_type_from_url(self, url: str) -> str:
        """Extract document type from URL"""
        url_lower = url.lower()
        if "transcript" in url_lower or "xmlread" in url_lower:
            return "Transcript"
        if "evidence" in url_lower or "evdread" in url_lower:
            return "Evidence"
        if "judgment" in url_lower or "verdict" in url_lower:
            return "Judgment"
        if "dissent" in url_lower:
            return "Dissent"
        if "book" in url_lower:
            return "Book/Research Material"
        return "Unknown"

    def _extract_text_content(self, soup: BeautifulSoup) -> str:
        """Extract main text content from page"""
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Try to find main content area
        content_selectors = [
            "main", "article", ".content", "#content",
            ".document-content", ".text-content"
        ]
        
        for selector in content_selectors:
            content = soup.select_one(selector)
            if content:
                return content.get_text(separator="\n", strip=True)
        
        # Fallback to body text
        body = soup.find("body")
        if body:
            return body.get_text(separator="\n", strip=True)
        
        return ""

    def _extract_metadata(self, soup: BeautifulSoup) -> Dict:
        """Extract metadata from page"""
        metadata = {}
        
        # Look for metadata in various formats
        meta_tags = soup.find_all("meta")
        for meta in meta_tags:
            name = meta.get("name") or meta.get("property")
            content = meta.get("content")
            if name and content:
                metadata[name] = content
        
        # Look for structured data
        # Implementation depends on site structure
        
        return metadata

    def _extract_volume_pages(self, soup: BeautifulSoup, url: str) -> Tuple[Optional[str], Optional[List[int]]]:
        """Extract volume and page numbers from document"""
        volume = None
        page_numbers = None
        
        # Try to extract from URL or content
        volume_match = re.search(r"[Vv]olume[:\s]*(\d+)", url + " " + soup.get_text())
        if volume_match:
            volume = volume_match.group(1)
        
        page_match = re.search(r"[Pp]age[:\s]*(\d+)", url + " " + soup.get_text())
        if page_match:
            page_numbers = [int(page_match.group(1))]
        
        return volume, page_numbers

    def get_all_documents(self) -> List[TokyoDocument]:
        """Get all scraped documents"""
        return self.documents

