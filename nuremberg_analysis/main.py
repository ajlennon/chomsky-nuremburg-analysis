#!/usr/bin/env python3
"""
Main Analysis Script

Comprehensive analysis tool for verifying Chomsky's claims against
Nuremberg Trials documents.

Copyright (C) 2025
License: GPL-3.0-or-later
"""

import argparse
import logging
import sys
from pathlib import Path

from nuremberg_analysis.chomsky_claims import ChomskyClaimsExtractor
from nuremberg_analysis.claim_verifier import ClaimVerifier
from nuremberg_analysis.document_scraper import NurembergDocumentScraper
from nuremberg_analysis.report_generator import ReportGenerator

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
log = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Verify Chomsky's claims against Nuremberg Trials documents"
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path("./reports"), help="Directory for output reports"
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path("./nuremberg_cache"),
        help="Directory for cached documents",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "html", "json", "all"],
        default="all",
        help="Output format for report",
    )
    parser.add_argument(
        "--rate-limit", type=float, default=1.0, help="Seconds to wait between HTTP requests"
    )
    parser.add_argument(
        "--skip-scraping", action="store_true", help="Skip web scraping, use cached documents only"
    )
    parser.add_argument(
        "--focus-claims",
        nargs="+",
        help="Only verify specific claim IDs (e.g., pal_001 yamashita_001)",
    )

    args = parser.parse_args()

    log.info("Starting Chomsky Claims Verification Analysis")
    log.info("=" * 60)

    # Extract claims
    log.info("Extracting claims from Chomsky's essay...")
    extractor = ChomskyClaimsExtractor()
    all_claims = extractor.get_all_claims()

    if args.focus_claims:
        claims_to_verify = [
            extractor.get_claim_by_id(cid)
            for cid in args.focus_claims
            if extractor.get_claim_by_id(cid) is not None
        ]
        log.info(f"Focusing on {len(claims_to_verify)} specific claims")
    else:
        claims_to_verify = all_claims
        log.info(f"Analyzing {len(claims_to_verify)} total claims")

    # Initialize scraper
    scraper = NurembergDocumentScraper(cache_dir=args.cache_dir, rate_limit=args.rate_limit)

    # Initialize verifier
    verifier = ClaimVerifier()

    # Initialize report generator
    report_gen = ReportGenerator(output_dir=args.output_dir)

    # Collect documents for each claim category
    log.info("\nCollecting relevant documents...")
    documents_by_category = {}

    if not args.skip_scraping:
        # Search for key documents
        log.info("Searching for Pal dissent documents...")
        pal_docs = scraper.find_pal_dissent()
        documents_by_category["Tokyo Trials - Justice Pal Dissent"] = pal_docs
        log.info(f"Found {len(pal_docs)} Pal-related documents")

        log.info("Searching for Yamashita documents...")
        yamashita_docs = scraper.find_yamashita_documents()
        documents_by_category["Tokyo Trials - General Yamashita"] = yamashita_docs
        log.info(f"Found {len(yamashita_docs)} Yamashita-related documents")

        log.info("Searching for Telford Taylor documents...")
        taylor_docs = scraper.find_telford_taylor_documents()
        documents_by_category["Nuremberg Principles - Telford Taylor"] = taylor_docs
        log.info(f"Found {len(taylor_docs)} Taylor-related documents")

        log.info("Searching for bombing-related documents...")
        bombing_docs = scraper.find_bombing_documents()
        documents_by_category["Nuremberg Principles - Operational Criterion"] = bombing_docs
        log.info(f"Found {len(bombing_docs)} bombing-related documents")

        # General search for other categories
        log.info("Performing general searches...")
        for claim in claims_to_verify:
            category = claim.category
            if category not in documents_by_category:
                # Search for documents related to this category
                query = " ".join(claim.keywords[:3])  # Use first 3 keywords
                docs = scraper.search_documents(query)
                documents_by_category[category] = docs
                log.info(f"Found {len(docs)} documents for category: {category}")
    else:
        log.info("Skipping web scraping, using cached documents only")
        # Load from cache if available
        # (Implementation would load cached documents)

    # Verify each claim
    log.info("\n" + "=" * 60)
    log.info("Verifying claims...")
    log.info("=" * 60)

    verification_results = []

    for i, claim in enumerate(claims_to_verify, 1):
        log.info(f"\n[{i}/{len(claims_to_verify)}] Verifying: {claim.id}")
        log.info(f"Category: {claim.category}")
        log.info(f"Claim: {claim.claim_text[:100]}...")

        # Get relevant documents for this claim's category
        relevant_docs = documents_by_category.get(claim.category, [])

        # Also search for documents matching claim keywords
        if not args.skip_scraping:
            keyword_query = " ".join(claim.keywords[:2])
            additional_docs = scraper.search_documents(keyword_query)
            relevant_docs.extend(additional_docs)

        # Remove duplicates
        seen_urls = set()
        unique_docs = []
        for doc in relevant_docs:
            if doc.url not in seen_urls:
                seen_urls.add(doc.url)
                unique_docs.append(doc)

        log.info(f"Analyzing {len(unique_docs)} relevant documents...")

        # Verify claim
        result = verifier.verify_claim(claim, unique_docs)
        verification_results.append(result)

        # Log result
        log.info(f"Status: {result.status} (Confidence: {result.confidence:.1%})")
        log.info(f"Supporting evidence: {len(result.supporting_evidence)}")
        log.info(f"Contradicting evidence: {len(result.contradicting_evidence)}")

    # Generate report
    log.info("\n" + "=" * 60)
    log.info("Generating report...")
    log.info("=" * 60)

    formats = ["markdown", "html", "json"] if args.format == "all" else [args.format]

    report_paths = []
    for fmt in formats:
        log.info(f"Generating {fmt} report...")
        report_path = report_gen.generate_comprehensive_report(
            verification_results, output_format=fmt
        )
        report_paths.append(report_path)
        log.info(f"Report saved to: {report_path}")

    # Summary
    log.info("\n" + "=" * 60)
    log.info("Analysis Complete!")
    log.info("=" * 60)

    verified = sum(1 for r in verification_results if r.status == "verified")
    partial = sum(1 for r in verification_results if r.status == "partially_verified")
    contradicted = sum(1 for r in verification_results if r.status == "contradicted")

    log.info("\nSummary:")
    log.info(f"  Total claims analyzed: {len(verification_results)}")
    log.info(f"  Verified: {verified}")
    log.info(f"  Partially verified: {partial}")
    log.info(f"  Contradicted: {contradicted}")
    log.info(
        f"  Insufficient evidence: {len(verification_results) - verified - partial - contradicted}"
    )

    log.info("\nReports generated:")
    for path in report_paths:
        log.info(f"  - {path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
