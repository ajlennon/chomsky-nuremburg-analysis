---
layout: page
title: Analysis Tool
permalink: /analysis/
---

## Analysis Tool

The project includes a comprehensive Python-based analysis tool for verifying claims against Harvard's Nuremberg Trials Project documents.

## Installation

```bash
# Install dependencies
pip install requests beautifulsoup4 lxml
```

## Usage

### Basic Usage

```bash
# Run full analysis
python3 -m nuremberg_analysis.main

# Generate reports in specific directory
python3 -m nuremberg_analysis.main --output-dir ./my_reports

# Use cached documents only (skip web scraping)
python3 -m nuremberg_analysis.main --skip-scraping

# Focus on specific claims
python3 -m nuremberg_analysis.main --focus-claims pal_001 pal_002 yamashita_001
```

### Command Line Options

- `--output-dir`: Directory for output reports (default: `./reports`)
- `--cache-dir`: Directory for cached documents (default: `./nuremberg_cache`)
- `--format`: Output format - `markdown`, `html`, `json`, or `all` (default: `all`)
- `--rate-limit`: Seconds to wait between HTTP requests (default: 1.0)
- `--skip-scraping`: Skip web scraping, use cached documents only
- `--focus-claims`: Only verify specific claim IDs

## Tool Structure

```
nuremberg_analysis/
├── __init__.py              # Package initialization
├── chomsky_claims.py        # Claim extraction and structuring
├── document_scraper.py      # Web scraper for Harvard website
├── claim_verifier.py        # Claim verification logic
├── report_generator.py      # Report generation
├── main.py                  # Main analysis script
└── test_basic.py            # Basic test suite
```

## Claims Analyzed

The tool analyzes **20 claims** across 8 categories:

1. **Tokyo Trials - General Yamashita** (1 claim)
2. **Tokyo Trials - Justice Pal Dissent** (5 claims)
3. **Nuremberg Principles - Operational Criterion** (4 claims)
4. **Nuremberg Trials - Admiral Gernetz Case** (1 claim)
5. **Nuremberg Principles - Telford Taylor** (4 claims)
6. **Nuremberg Principles - Ex Post Facto** (1 claim)
7. **Tokyo Trials - General Assessment** (3 claims)
8. **American Presidents - Context** (1 claim)

## Report Format

Reports include:

- **Executive Summary**: Overview of verification status
- **Detailed Results**: Claim-by-claim verification with:
  - Claim text and context
  - Verification status (verified/partially verified/contradicted/insufficient evidence)
  - Confidence level
  - Supporting evidence excerpts
  - Contradicting evidence excerpts
  - Citations and references
- **Methodology**: Description of analysis approach
- **Citations**: Complete list of document sources

## Example Output

After running the analysis, you'll get:

```
reports/
├── chomsky_verification_report_YYYYMMDD_HHMMSS.md
├── chomsky_verification_report_YYYYMMDD_HHMMSS.html
└── chomsky_verification_report_YYYYMMDD_HHMMSS.json

nuremberg_cache/
└── [cached HTML documents]
```

## Features

- **Comprehensive**: Analyzes all 20 claims from Chomsky's essay
- **Automated**: Automated document search and verification
- **Cached**: Documents are cached for offline analysis
- **Multiple Formats**: Reports in Markdown, HTML, and JSON
- **Respectful**: Rate-limited requests to be respectful to Harvard's servers
- **Well-Documented**: Comprehensive documentation and examples

## Limitations

- **Website Structure**: The scraper depends on the Harvard website structure - changes may require updates
- **Document Access**: Some documents may require special access or may not be fully digitized
- **External Sources**: Some claims (e.g., about Telford Taylor's book) may require consulting external sources
- **Automated Analysis**: This is an automated tool. Full verification may require manual review of original documents

## Ethical Considerations

This tool analyzes historical documents related to war crimes trials. Users should:

- Be aware that documents contain graphic descriptions of violence and genocide
- Use the tool responsibly and verify claims through original sources
- Understand that automated analysis has limitations
- Consult academic sources for comprehensive understanding

