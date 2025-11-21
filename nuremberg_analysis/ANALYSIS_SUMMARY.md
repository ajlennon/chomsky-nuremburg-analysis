# Analysis Tool Summary

## What Was Created

A comprehensive analysis tool to verify all claims in Noam Chomsky's essay "If the Nuremberg Laws were Applied..." against documents from the Harvard Law School Library's Nuremberg Trials Project.

## Components

### 1. Claim Extraction (`chomsky_claims.py`)
- Extracts and structures **20 distinct claims** from Chomsky's essay
- Organizes claims into categories:
  - Tokyo Trials - General Yamashita (1 claim)
  - Tokyo Trials - Justice Pal Dissent (5 claims)
  - Nuremberg Principles - Operational Criterion (4 claims)
  - Nuremberg Trials - Admiral Gernetz Case (1 claim)
  - Nuremberg Principles - Telford Taylor (4 claims)
  - Nuremberg Principles - Ex Post Facto (1 claim)
  - Tokyo Trials - General Assessment (3 claims)
  - American Presidents - Context (1 claim)

### 2. Document Scraper (`document_scraper.py`)
- Web scraper for Harvard Nuremberg Trials Project website
- Features:
  - Rate-limited requests (respectful scraping)
  - Document caching for offline analysis
  - Specialized search functions:
    - `find_pal_dissent()` - Search for Justice Pal's dissent
    - `find_yamashita_documents()` - Search for Yamashita case documents
    - `find_telford_taylor_documents()` - Search for Telford Taylor references
    - `find_bombing_documents()` - Search for bombing-related discussions
  - Extracts text content, metadata, and page images
  - Handles different document types (transcripts, briefs, judgments, etc.)

### 3. Claim Verifier (`claim_verifier.py`)
- Verifies each claim against collected documents
- Features:
  - Relevance scoring for documents
  - Evidence extraction (supporting and contradicting)
  - Confidence scoring
  - Status determination:
    - ✅ Verified
    - ⚠️ Partially Verified
    - ❌ Contradicted
    - ❓ Insufficient Evidence
    - 🔍 Not Found

### 4. Report Generator (`report_generator.py`)
- Generates comprehensive reports in multiple formats:
  - **Markdown**: Human-readable with formatting
  - **HTML**: Web-friendly version
  - **JSON**: Machine-readable for further analysis
- Includes:
  - Executive summary with statistics
  - Detailed claim-by-claim verification
  - Evidence excerpts with citations
  - Complete bibliography
  - Methodology and disclaimers

### 5. Main Script (`main.py`)
- Command-line interface for running analysis
- Options for:
  - Focused analysis (specific claims)
  - Cached document usage
  - Custom output locations
  - Rate limiting
  - Output format selection

## Key Claims to Verify

### High Priority Claims

1. **Pal's Dissent on Atom Bombs** (`pal_004`)
   - Claim: Pal compared atom bombs to Nazi crimes
   - Documents needed: Pal's full dissent (700 pages)

2. **Yamashita Command Responsibility** (`yamashita_001`)
   - Claim: Yamashita hanged for atrocities by troops he had no contact with
   - Documents needed: Yamashita judgment, trial transcripts

3. **Operational Criterion** (`criterion_001`)
   - Claim: War crimes determined by "if enemy did it and we didn't"
   - Documents needed: Telford Taylor's "Nuremberg and Vietnam", trial documents

4. **Gernetz/Nimitz Case** (`gernetz_001`)
   - Claim: Gernetz acquitted because Nimitz testified US did similar things
   - Documents needed: Gernetz trial transcripts, Nimitz testimony

## Usage

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run full analysis
python3 -m nuremberg_analysis.main

# View reports
ls reports/
```

### Focused Analysis

```bash
# Focus on Pal dissent claims
python3 -m nuremberg_analysis.main --focus-claims pal_001 pal_002 pal_003 pal_004 pal_005
```

## Expected Challenges

1. **Website Structure**: Harvard website may have changed structure - scraper may need updates
2. **Document Access**: Some documents may require special access or login
3. **Search Limitations**: Website search may not find all relevant documents
4. **External Sources**: Some claims (e.g., Telford Taylor's book) require external sources
5. **Full Text Access**: Some documents may only have metadata, not full text

## Next Steps

1. **Run Initial Analysis**: Execute the tool to see what documents are found
2. **Review Results**: Check which claims have sufficient evidence
3. **Manual Verification**: For high-priority claims, manually review original documents
4. **External Sources**: Consult Telford Taylor's book and Yale Law Journal article
5. **Refinement**: Update scraper based on actual website structure
6. **Enhancement**: Improve claim verification logic based on initial results

## Output Structure

Reports will be generated in `./reports/` directory:

```
reports/
├── chomsky_verification_report_YYYYMMDD_HHMMSS.md
├── chomsky_verification_report_YYYYMMDD_HHMMSS.html
└── chomsky_verification_report_YYYYMMDD_HHMMSS.json
```

Each report includes:
- Executive summary with verification statistics
- Detailed results for each of 20 claims
- Evidence excerpts with citations
- Complete bibliography
- Methodology and disclaimers

## Notes

- The tool respects rate limits (default 1 second between requests)
- Documents are cached for offline analysis
- The analysis is automated - manual review recommended for important claims
- Some claims may require consulting external sources (books, articles)
- Full verification may require access to original documents at Harvard Law Library

