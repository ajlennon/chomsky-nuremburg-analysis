# Usage Examples

## Basic Analysis

Run a complete analysis of all claims:

```bash
python3 -m nuremberg_analysis.main
```

This will:
1. Extract all claims from Chomsky's essay
2. Search the Harvard website for relevant documents
3. Verify each claim against found documents
4. Generate comprehensive reports in Markdown, HTML, and JSON formats

## Focused Analysis

Analyze only specific claims:

```bash
# Focus on Pal dissent claims
python3 -m nuremberg_analysis.main --focus-claims pal_001 pal_002 pal_003 pal_004 pal_005

# Focus on Yamashita claims
python3 -m nuremberg_analysis.main --focus-claims yamashita_001

# Focus on Telford Taylor claims
python3 -m nuremberg_analysis.main --focus-claims taylor_001 taylor_002 taylor_003 taylor_004
```

## Using Cached Documents

If you've already scraped documents, skip web scraping:

```bash
python3 -m nuremberg_analysis.main --skip-scraping
```

## Custom Output Locations

Specify custom directories for reports and cache:

```bash
python3 -m nuremberg_analysis.main \
    --output-dir ./my_reports \
    --cache-dir ./my_cache
```

## Rate Limiting

Adjust the rate limit between requests (be respectful to the Harvard website):

```bash
# Wait 2 seconds between requests
python3 -m nuremberg_analysis.main --rate-limit 2.0
```

## Output Formats

Generate reports in specific formats:

```bash
# Markdown only
python3 -m nuremberg_analysis.main --format markdown

# HTML only
python3 -m nuremberg_analysis.main --format html

# JSON only (for programmatic processing)
python3 -m nuremberg_analysis.main --format json

# All formats (default)
python3 -m nuremberg_analysis.main --format all
```

## Programmatic Usage

You can also use the modules programmatically:

```python
from nuremberg_analysis.chomsky_claims import ChomskyClaimsExtractor
from nuremberg_analysis.document_scraper import NurembergDocumentScraper
from nuremberg_analysis.claim_verifier import ClaimVerifier

# Extract claims
extractor = ChomskyClaimsExtractor()
claims = extractor.get_all_claims()

# Search for documents
scraper = NurembergDocumentScraper()
pal_docs = scraper.find_pal_dissent()

# Verify a claim
verifier = ClaimVerifier()
result = verifier.verify_claim(claims[0], pal_docs)

print(f"Status: {result.status}")
print(f"Confidence: {result.confidence:.1%}")
print(f"Supporting evidence: {len(result.supporting_evidence)}")
```

## Expected Output

After running the analysis, you'll find:

```
reports/
├── chomsky_verification_report_20250115_143022.md
├── chomsky_verification_report_20250115_143022.html
└── chomsky_verification_report_20250115_143022.json

nuremberg_cache/
├── [cached HTML documents]
```

The Markdown report includes:
- Executive summary with statistics
- Detailed verification results for each claim
- Supporting and contradicting evidence excerpts
- Complete citations
- Methodology and disclaimers

