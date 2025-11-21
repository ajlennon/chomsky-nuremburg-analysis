"""
Claim Verifier

Verifies Chomsky's claims against Nuremberg Trials documents.

Copyright (C) 2025
License: GPL-3.0-or-later
"""

import logging
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from nuremberg_analysis.chomsky_claims import Claim
from nuremberg_analysis.document_scraper import Document

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


@dataclass
class VerificationResult:
    """Result of verifying a claim against documents"""

    claim: Claim
    status: str  # "verified", "partially_verified", "contradicted", "insufficient_evidence", "not_found"
    confidence: float  # 0.0 to 1.0
    supporting_evidence: List[Tuple[Document, str]]  # (document, excerpt)
    contradicting_evidence: List[Tuple[Document, str]]
    notes: str
    citations: List[str]


class ClaimVerifier:
    """Verifies claims against documents"""

    def __init__(self):
        self.verification_results: Dict[str, VerificationResult] = {}

    def verify_claim(self, claim: Claim, documents: List[Document]) -> VerificationResult:
        """
        Verify a single claim against documents

        Args:
            claim: The claim to verify
            documents: List of relevant documents

        Returns:
            VerificationResult
        """
        log.info(f"Verifying claim: {claim.id} - {claim.category}")

        supporting_evidence = []
        contradicting_evidence = []
        citations = []

        # Search for relevant content in documents
        for doc in documents:
            if not doc.text_content:
                continue

            # Check if document is relevant
            relevance_score = self._calculate_relevance(claim, doc)
            if relevance_score < 0.3:
                continue

            # Extract relevant excerpts
            excerpts = self._find_relevant_excerpts(claim, doc)

            for excerpt, is_supporting in excerpts:
                if is_supporting:
                    supporting_evidence.append((doc, excerpt))
                    citations.append(f"{doc.title} ({doc.url})")
                else:
                    contradicting_evidence.append((doc, excerpt))
                    citations.append(f"{doc.title} ({doc.url})")

        # Determine verification status
        status, confidence = self._determine_status(
            claim, supporting_evidence, contradicting_evidence
        )

        # Generate notes
        notes = self._generate_notes(claim, supporting_evidence, contradicting_evidence)

        result = VerificationResult(
            claim=claim,
            status=status,
            confidence=confidence,
            supporting_evidence=supporting_evidence,
            contradicting_evidence=contradicting_evidence,
            notes=notes,
            citations=citations,
        )

        self.verification_results[claim.id] = result
        return result

    def _calculate_relevance(self, claim: Claim, doc: Document) -> float:
        """Calculate how relevant a document is to a claim"""
        score = 0.0
        text = (doc.text_content or "").lower()
        title = doc.title.lower()

        # Check keyword matches
        keyword_matches = sum(
            1 for kw in claim.keywords if kw.lower() in text or kw.lower() in title
        )
        score += keyword_matches / max(len(claim.keywords), 1) * 0.5

        # Check trial match
        if claim.category.startswith("Tokyo"):
            if "tokyo" in text.lower() or "tokyo" in doc.trial.lower():
                score += 0.3
        elif "Nuremberg" in claim.category:
            if "nuremberg" in text.lower() or "imt" in doc.trial.lower():
                score += 0.3

        # Check document type match
        if "dissent" in claim.category.lower() and "dissent" in doc.document_type.lower():
            score += 0.2

        return min(score, 1.0)

    def _find_relevant_excerpts(
        self, claim: Claim, doc: Document, context_chars: int = 200
    ) -> List[Tuple[str, bool]]:
        """
        Find relevant excerpts from document

        Returns:
            List of (excerpt, is_supporting) tuples
        """
        excerpts = []
        text = doc.text_content or ""
        text_lower = text.lower()

        # Search for keywords
        for keyword in claim.keywords:
            keyword_lower = keyword.lower()
            if keyword_lower not in text_lower:
                continue

            # Find all occurrences
            for match in re.finditer(re.escape(keyword_lower), text_lower):
                start = max(0, match.start() - context_chars)
                end = min(len(text), match.end() + context_chars)
                excerpt = text[start:end]

                # Determine if supporting or contradicting
                is_supporting = self._is_excerpt_supporting(claim, excerpt)
                excerpts.append((excerpt, is_supporting))

        # Also search for claim-specific patterns
        excerpts.extend(self._find_claim_specific_excerpts(claim, doc))

        return excerpts

    def _find_claim_specific_excerpts(self, claim: Claim, doc: Document) -> List[Tuple[str, bool]]:
        """Find excerpts specific to certain claim types"""
        excerpts = []
        text = doc.text_content or ""

        # Pal dissent specific searches
        if "pal" in claim.id:
            # Look for mentions of atom bomb in context of Pal
            if "atom" in text.lower() or "atomic" in text.lower():
                # Find context around atom bomb mentions
                for match in re.finditer(r"atom(ic)?\s+bomb", text, re.IGNORECASE):
                    start = max(0, match.start() - 300)
                    end = min(len(text), match.end() + 300)
                    excerpt = text[start:end]
                    # Check if Pal is mentioned nearby
                    if "pal" in excerpt.lower() or "indian" in excerpt.lower():
                        excerpts.append((excerpt, True))

        # Yamashita specific searches
        if "yamashita" in claim.id:
            # Look for mentions of command responsibility
            for match in re.finditer(r"command|responsibility|contact", text, re.IGNORECASE):
                start = max(0, match.start() - 300)
                end = min(len(text), match.end() + 300)
                excerpt = text[start:end]
                if "yamashita" in excerpt.lower():
                    excerpts.append((excerpt, True))

        # Telford Taylor specific searches
        if "taylor" in claim.id:
            # Look for mentions of operational criterion or similar concepts
            patterns = [
                r"operational\s+criterion",
                r"war\s+crime.*enemy",
                r"if.*enemy.*done",
                r"bombing.*not.*war\s+crime",
            ]
            for pattern in patterns:
                for match in re.finditer(pattern, text, re.IGNORECASE):
                    start = max(0, match.start() - 300)
                    end = min(len(text), match.end() + 300)
                    excerpt = text[start:end]
                    if "taylor" in excerpt.lower():
                        excerpts.append((excerpt, True))

        return excerpts

    def _is_excerpt_supporting(self, claim: Claim, excerpt: str) -> bool:
        """Determine if an excerpt supports or contradicts the claim"""
        excerpt_lower = excerpt.lower()

        # Simple heuristics - can be improved
        # Look for negation words
        negation_words = [
            "not",
            "never",
            "no",
            "neither",
            "nor",
            "cannot",
            "can't",
            "didn't",
            "wasn't",
        ]
        has_negation = any(word in excerpt_lower for word in negation_words)

        # This is a simplified check - real implementation would need more sophisticated NLP
        # For now, assume excerpts are supporting unless clearly contradictory
        return True  # Simplified - would need better logic

    def _determine_status(
        self, claim: Claim, supporting: List, contradicting: List
    ) -> Tuple[str, float]:
        """
        Determine verification status and confidence

        Returns:
            (status, confidence) tuple
        """
        if len(supporting) == 0 and len(contradicting) == 0:
            return ("not_found", 0.0)

        if len(supporting) > 0 and len(contradicting) == 0:
            confidence = min(0.5 + (len(supporting) * 0.1), 1.0)
            return ("verified", confidence)

        if len(supporting) > 0 and len(contradicting) > 0:
            ratio = len(supporting) / (len(supporting) + len(contradicting))
            confidence = abs(ratio - 0.5) * 2  # Higher confidence the more one-sided
            return ("partially_verified", confidence)

        if len(supporting) == 0 and len(contradicting) > 0:
            return ("contradicted", 0.7)

        return ("insufficient_evidence", 0.3)

    def _generate_notes(self, claim: Claim, supporting: List, contradicting: List) -> str:
        """Generate notes about the verification"""
        notes = []

        if len(supporting) > 0:
            notes.append(f"Found {len(supporting)} supporting evidence excerpt(s).")

        if len(contradicting) > 0:
            notes.append(f"Found {len(contradicting)} contradicting evidence excerpt(s).")

        if len(supporting) == 0 and len(contradicting) == 0:
            notes.append("No relevant evidence found in available documents.")
            notes.append("May require access to additional documents or external sources.")

        # Add claim-specific notes
        if "pal" in claim.id:
            notes.append("Pal's dissent is a key document - full text review recommended.")

        if "yamashita" in claim.id:
            notes.append(
                "Yamashita case involves command responsibility doctrine - check judgment text."
            )

        if "taylor" in claim.id:
            notes.append(
                "Telford Taylor's book 'Nuremberg and Vietnam' may need to be consulted separately."
            )

        return " ".join(notes)
