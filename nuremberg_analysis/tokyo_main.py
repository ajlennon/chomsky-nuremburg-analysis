"""
Tokyo Trials Analysis Main Script

Analyzes Chomsky's Tokyo Trials claims against available archives.

Copyright (C) 2025
License: GPL-3.0-or-later
"""

import logging
from pathlib import Path
from typing import List

from nuremberg_analysis.chomsky_claims import ChomskyClaimsExtractor
from nuremberg_analysis.tokyo_scraper import TokyoDocumentScraper, TokyoDocument
from nuremberg_analysis.tokyo_verifier import TokyoClaimVerifier

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)


def get_tokyo_claims():
    """Get all Tokyo Trials-related claims"""
    extractor = ChomskyClaimsExtractor()
    all_claims = extractor.get_all_claims()
    
    # Filter for Tokyo Trials claims
    tokyo_claims = [
        claim for claim in all_claims
        if "Tokyo" in claim.category or "Yamashita" in claim.category or "Pal" in claim.category
    ]
    
    return tokyo_claims


def analyze_tokyo_claims():
    """Main analysis function"""
    log.info("Starting Tokyo Trials analysis")
    
    # Get Tokyo Trials claims
    tokyo_claims = get_tokyo_claims()
    log.info(f"Found {len(tokyo_claims)} Tokyo Trials claims to analyze")
    
    # Initialize scraper
    scraper = TokyoDocumentScraper(cache_dir=Path("./tokyo_cache"))
    
    # Search for Pal's dissent
    log.info("Searching for Pal's dissent documents...")
    pal_docs = scraper.search_pal_dissent()
    log.info(f"Found {len(pal_docs)} Pal-related documents")
    
    # Search for Yamashita documents
    log.info("Searching for Yamashita case documents...")
    yamashita_docs = scraper.search_yamashita()
    log.info(f"Found {len(yamashita_docs)} Yamashita-related documents")
    
    # Search trial transcripts for relevant keywords
    keywords = ["Pal", "dissent", "atom bomb", "Yamashita", "command responsibility"]
    log.info(f"Searching trial transcripts for keywords: {keywords}")
    transcript_docs = scraper.search_trial_transcripts(keywords, max_results=50)
    log.info(f"Found {len(transcript_docs)} relevant transcript documents")
    
    # Combine all documents
    all_docs = pal_docs + yamashita_docs + transcript_docs
    log.info(f"Total documents found: {len(all_docs)}")
    
    # Verify claims against documents
    log.info("Verifying claims against documents...")
    verifier = TokyoClaimVerifier()
    verification_results = {}
    
    for claim in tokyo_claims:
        result = verifier.verify_claim(claim, all_docs)
        verification_results[claim.id] = result
        log.info(f"  {claim.id}: {result.status} (confidence: {result.confidence:.1%})")
    
    # Print summary
    print("\n" + "="*80)
    print("TOKYO TRIALS ANALYSIS SUMMARY")
    print("="*80)
    print(f"\nClaims to analyze: {len(tokyo_claims)}")
    print(f"Documents found: {len(all_docs)}")
    
    print("\nTokyo Trials Claims:")
    for claim in tokyo_claims:
        print(f"  - {claim.id}: {claim.category}")
        print(f"    {claim.claim_text[:100]}...")
    
    print("\nDocuments Found:")
    for doc in all_docs[:10]:  # Show first 10
        print(f"  - {doc.title}")
        print(f"    Source: {doc.source}, Type: {doc.document_type}")
        print(f"    URL: {doc.url}")
    
    if len(all_docs) > 10:
        print(f"\n  ... and {len(all_docs) - 10} more documents")
    
    print("\n" + "="*80)
    print("VERIFICATION RESULTS")
    print("="*80)
    
    verified_count = sum(1 for r in verification_results.values() if r.status == "verified")
    partial_count = sum(1 for r in verification_results.values() if r.status == "partially_verified")
    not_found_count = sum(1 for r in verification_results.values() if r.status == "not_found")
    
    print(f"\nVerified: {verified_count}")
    print(f"Partially Verified: {partial_count}")
    print(f"Not Found: {not_found_count}")
    
    print("\nDetailed Results:")
    for claim_id, result in verification_results.items():
        claim = result.claim
        print(f"\n  {claim_id}: {claim.category}")
        print(f"    Status: {result.status} (confidence: {result.confidence:.1%})")
        print(f"    Supporting evidence: {len(result.supporting_evidence)} excerpts")
        if result.supporting_evidence:
            print(f"    First excerpt: {result.supporting_evidence[0][1][:150]}...")
        print(f"    Notes: {result.notes}")
    
    print("\n" + "="*80)
    print("\nNote: Full verification requires:")
    print("  1. Access to Tokyo Trial Database (may require subscription)")
    print("  2. Access to University of Wisconsin database (subscription)")
    print("  3. Manual review of Pal's dissent document")
    print("  4. Review of Yamashita trial records (separate from Tokyo Trials)")
    print("\n" + "="*80)
    
    return {
        "claims": tokyo_claims,
        "documents": all_docs,
        "pal_documents": pal_docs,
        "yamashita_documents": yamashita_docs,
        "transcript_documents": transcript_docs,
        "verification_results": verification_results,
    }


if __name__ == "__main__":
    results = analyze_tokyo_claims()
    
    # Save results summary
    output_file = Path("./tokyo_analysis_summary.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("TOKYO TRIALS ANALYSIS SUMMARY\n")
        f.write("="*80 + "\n\n")
        f.write(f"Claims analyzed: {len(results['claims'])}\n")
        f.write(f"Total documents found: {len(results['documents'])}\n\n")
        
        f.write("CLAIMS:\n")
        for claim in results['claims']:
            f.write(f"\n{claim.id}: {claim.category}\n")
            f.write(f"  {claim.claim_text}\n")
        
        f.write("\n\nDOCUMENTS FOUND:\n")
        for doc in results['documents']:
            f.write(f"\n{doc.title}\n")
            f.write(f"  Source: {doc.source}\n")
            f.write(f"  Type: {doc.document_type}\n")
            f.write(f"  URL: {doc.url}\n")
            if doc.text_content:
                f.write(f"  Content length: {len(doc.text_content)} characters\n")
        
        f.write("\n\nVERIFICATION RESULTS:\n")
        for claim_id, result in results['verification_results'].items():
            f.write(f"\n{claim_id}: {result.claim.category}\n")
            f.write(f"  Status: {result.status}\n")
            f.write(f"  Confidence: {result.confidence:.1%}\n")
            f.write(f"  Supporting evidence: {len(result.supporting_evidence)} excerpts\n")
            f.write(f"  Notes: {result.notes}\n")
            if result.supporting_evidence:
                f.write(f"  First excerpt: {result.supporting_evidence[0][1][:200]}...\n")
    
    log.info(f"Analysis summary saved to {output_file}")

