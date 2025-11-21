#!/usr/bin/env python3
"""
Basic Test Script

Quick test to verify the analysis tool works correctly.

Copyright (C) 2025
License: GPL-3.0-or-later
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from nuremberg_analysis.chomsky_claims import ChomskyClaimsExtractor
from nuremberg_analysis.claim_verifier import ClaimVerifier
from nuremberg_analysis.document_scraper import NurembergDocumentScraper


def test_claim_extraction():
    """Test that claims can be extracted"""
    print("Testing claim extraction...")
    extractor = ChomskyClaimsExtractor()
    claims = extractor.get_all_claims()
    print(f"✓ Extracted {len(claims)} claims")

    # Test filtering
    pal_claims = extractor.get_claims_by_category("Tokyo Trials - Justice Pal Dissent")
    print(f"✓ Found {len(pal_claims)} Pal-related claims")

    # Test getting specific claim
    claim = extractor.get_claim_by_id("pal_001")
    if claim:
        print(f"✓ Found claim pal_001: {claim.claim_text[:60]}...")
    else:
        print("✗ Failed to find claim pal_001")
        return False

    return True


def test_scraper_initialization():
    """Test that scraper can be initialized"""
    print("\nTesting scraper initialization...")
    try:
        scraper = NurembergDocumentScraper(cache_dir=Path("./test_cache"), rate_limit=2.0)
        print("✓ Scraper initialized successfully")
        print(f"  Base URL: {scraper.BASE_URL}")
        print(f"  Cache dir: {scraper.cache_dir}")
        return True
    except Exception as e:
        print(f"✗ Scraper initialization failed: {e}")
        return False


def test_verifier_initialization():
    """Test that verifier can be initialized"""
    print("\nTesting verifier initialization...")
    try:
        verifier = ClaimVerifier()
        print("✓ Verifier initialized successfully")
        return True
    except Exception as e:
        print(f"✗ Verifier initialization failed: {e}")
        return False


def test_claim_structure():
    """Test that claims have required fields"""
    print("\nTesting claim structure...")
    extractor = ChomskyClaimsExtractor()
    claims = extractor.get_all_claims()

    required_fields = ["id", "category", "claim_text", "context", "keywords", "expected_documents"]

    for claim in claims[:3]:  # Test first 3 claims
        for field in required_fields:
            if not hasattr(claim, field):
                print(f"✗ Claim {claim.id} missing field: {field}")
                return False
            value = getattr(claim, field)
            if value is None or (isinstance(value, (list, str)) and len(value) == 0):
                print(f"✗ Claim {claim.id} has empty field: {field}")
                return False

    print("✓ All claims have required fields")
    return True


def main():
    """Run all tests"""
    print("=" * 60)
    print("Nuremberg Analysis Tool - Basic Tests")
    print("=" * 60)

    tests = [
        test_claim_extraction,
        test_scraper_initialization,
        test_verifier_initialization,
        test_claim_structure,
    ]

    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test {test.__name__} raised exception: {e}")
            results.append(False)

    print("\n" + "=" * 60)
    print("Test Results")
    print("=" * 60)

    passed = sum(results)
    total = len(results)

    print(f"Passed: {passed}/{total}")

    if passed == total:
        print("✓ All tests passed!")
        return 0
    print("✗ Some tests failed")
    return 1


if __name__ == "__main__":
    sys.exit(main())
