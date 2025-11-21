"""
Tokyo Trials Claim Verifier

Verifies Chomsky's Tokyo Trials claims against available documents.

Copyright (C) 2025
License: GPL-3.0-or-later
"""

import logging
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from nuremberg_analysis.chomsky_claims import Claim
from nuremberg_analysis.tokyo_scraper import TokyoDocument

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


@dataclass
class TokyoVerificationResult:
    """Result of verifying a Tokyo Trials claim"""

    claim: Claim
    status: str  # "verified", "partially_verified", "contradicted", "insufficient_evidence", "not_found"
    confidence: float  # 0.0 to 1.0
    supporting_evidence: List[Tuple[TokyoDocument, str]]  # (document, excerpt)
    contradicting_evidence: List[Tuple[TokyoDocument, str]]
    notes: str
    citations: List[str]


class TokyoClaimVerifier:
    """Verifies Tokyo Trials claims against documents"""

    def __init__(self):
        self.verification_results: Dict[str, TokyoVerificationResult] = {}

    def verify_claim(self, claim: Claim, documents: List[TokyoDocument]) -> TokyoVerificationResult:
        """
        Verify a single claim against documents

        Args:
            claim: The claim to verify
            documents: List of relevant documents

        Returns:
            TokyoVerificationResult
        """
        log.info(f"Verifying Tokyo claim: {claim.id} - {claim.category}")

        supporting_evidence = []
        contradicting_evidence = []
        citations = []

        # Search for relevant content in documents
        for doc in documents:
            if not doc.text_content:
                continue

            # Check if document is relevant
            relevance_score = self._calculate_relevance(claim, doc)
            if relevance_score < 0.2:
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

        result = TokyoVerificationResult(
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

    def _calculate_relevance(self, claim: Claim, doc: TokyoDocument) -> float:
        """Calculate how relevant a document is to a claim"""
        score = 0.0
        text = (doc.text_content or "").lower()
        title = (doc.title or "").lower()

        # Check keywords
        for keyword in claim.keywords:
            keyword_lower = keyword.lower()
            if keyword_lower in title:
                score += 0.3
            if keyword_lower in text:
                score += 0.1

        # Check category-specific relevance
        if "Pal" in claim.category and ("pal" in title or "pal" in text or "dissent" in title.lower()):
            score += 0.5
        if "Yamashita" in claim.category and "yamashita" in text.lower():
            score += 0.5
        if "atom bomb" in claim.claim_text.lower() and ("atom" in text or "bomb" in text or "hiroshima" in text or "nagasaki" in text):
            score += 0.4

        return min(score, 1.0)

    def _find_relevant_excerpts(self, claim: Claim, doc: TokyoDocument) -> List[Tuple[str, bool]]:
        """Find relevant excerpts from document"""
        excerpts = []
        text = doc.text_content or ""
        
        if not text:
            return excerpts

        # Search for claim keywords
        keywords = [k.lower() for k in claim.keywords]
        claim_text_lower = claim.claim_text.lower()

        # Look for sentences containing keywords
        sentences = re.split(r'[.!?]\s+', text)
        
        for sentence in sentences:
            sentence_lower = sentence.lower()
            relevance = 0
            
            # Check for keyword matches
            for keyword in keywords:
                if keyword.lower() in sentence_lower:
                    relevance += 1
            
            # Check for claim-specific patterns
            if "pal" in claim.category.lower():
                if "pal" in sentence_lower or "dissent" in sentence_lower:
                    relevance += 2
                if "atom" in sentence_lower and "bomb" in sentence_lower:
                    relevance += 3
                if "nazi" in sentence_lower and ("crime" in sentence_lower or "atrocity" in sentence_lower):
                    relevance += 2
            
            if "yamashita" in claim.category.lower():
                if "yamashita" in sentence_lower:
                    relevance += 2
                if "command" in sentence_lower and "responsibility" in sentence_lower:
                    relevance += 2
            
            if relevance > 0:
                # Determine if supporting or contradicting
                is_supporting = self._is_supporting(claim, sentence)
                excerpts.append((sentence.strip(), is_supporting))
        
        return excerpts[:10]  # Limit to 10 excerpts

    def _is_supporting(self, claim: Claim, text: str) -> bool:
        """Determine if text supports the claim"""
        text_lower = text.lower()
        claim_lower = claim.claim_text.lower()
        
        # Simple heuristics
        negative_words = ["not", "no", "never", "disagree", "reject", "deny"]
        
        # Check for negative indicators
        for neg_word in negative_words:
            if neg_word in text_lower and any(kw.lower() in text_lower for kw in claim.keywords):
                return False
        
        # If keywords are present, likely supporting
        return True

    def _determine_status(
        self,
        claim: Claim,
        supporting: List[Tuple[TokyoDocument, str]],
        contradicting: List[Tuple[TokyoDocument, str]],
    ) -> Tuple[str, float]:
        """Determine verification status and confidence"""
        support_count = len(supporting)
        contradict_count = len(contradicting)

        if support_count == 0 and contradict_count == 0:
            return "not_found", 0.0

        if contradict_count > support_count * 2:
            return "contradicted", 0.3

        if support_count > 0:
            # Calculate confidence based on evidence quality
            confidence = min(0.3 + (support_count * 0.1), 0.9)
            
            if support_count >= 3:
                return "verified", confidence
            elif support_count >= 1:
                return "partially_verified", confidence
        
        return "insufficient_evidence", 0.2

    def _generate_notes(
        self,
        claim: Claim,
        supporting: List[Tuple[TokyoDocument, str]],
        contradicting: List[Tuple[TokyoDocument, str]],
    ) -> str:
        """Generate notes about verification"""
        notes = []
        
        if len(supporting) > 0:
            notes.append(f"Found {len(supporting)} supporting evidence excerpts.")
        if len(contradicting) > 0:
            notes.append(f"Found {len(contradicting)} contradicting evidence excerpts.")
        
        # Add specific notes based on claim
        if "Pal" in claim.category:
            notes.append("Pal's dissent document may require full text access for complete verification.")
        if "Yamashita" in claim.category:
            notes.append("Yamashita was tried separately from Tokyo Trials - may require separate archive search.")
        
        if len(notes) == 0:
            notes.append("No relevant evidence found in available documents.")
        
        return " ".join(notes)

