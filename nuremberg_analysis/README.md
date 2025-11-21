# Nuremberg Trials Analysis Tool

A comprehensive tool for analyzing and verifying claims against the Harvard Law School Library's Nuremberg Trials Project documents.

## Overview

This tool verifies claims made in Noam Chomsky's essay "If the Nuremberg Laws were Applied..." against actual documents from the Nuremberg and Tokyo Trials. It provides:

- **Automated document scraping** from the Harvard Law School Library's Nuremberg Trials Project
- **Claim extraction and structuring** from Chomsky's essay
- **Document search and analysis** to find relevant evidence
- **Comprehensive verification reports** with citations and evidence excerpts

## Features

- Extracts and structures all claims from Chomsky's essay
- Searches the Harvard Nuremberg Trials Project website for relevant documents
- Verifies each claim against found documents
- Generates comprehensive reports in multiple formats (Markdown, HTML, JSON)
- Provides citations and evidence excerpts for each claim
- Caches documents for offline analysis

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Make main script executable
chmod +x nuremberg_analysis/main.py
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

## Structure

```
nuremberg_analysis/
├── __init__.py              # Package initialization
├── chomsky_claims.py        # Claim extraction and structuring
├── document_scraper.py      # Web scraper for Harvard website
├── claim_verifier.py        # Claim verification logic
├── report_generator.py      # Report generation
└── main.py                  # Main analysis script
```

## Claims Analyzed

The tool analyzes claims in the following categories:

1. **Tokyo Trials - General Yamashita**: Claims about General Yamashita's trial and execution
2. **Tokyo Trials - Justice Pal Dissent**: Claims about Justice Radhabinod Pal's dissent
3. **Nuremberg Principles - Operational Criterion**: Claims about how war crimes were determined
4. **Nuremberg Trials - Admiral Gernetz Case**: Claims about the Gernetz/Nimitz case
5. **Nuremberg Principles - Telford Taylor**: Claims about Telford Taylor's statements
6. **Tokyo Trials - General Assessment**: Claims about the Tokyo Tribunal

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

## Limitations

- **Automated Analysis**: This is an automated tool. Full verification may require manual review of original documents
- **Website Structure**: The scraper depends on the Harvard website structure - changes may require updates
- **Document Access**: Some documents may require special access or may not be fully digitized
- **External Sources**: Some claims (e.g., about Telford Taylor's book) may require consulting external sources

## Ethical Considerations

This tool analyzes historical documents related to war crimes trials. Users should:

- Be aware that documents contain graphic descriptions of violence and genocide
- Use the tool responsibly and verify claims through original sources
- Understand that automated analysis has limitations
- Consult academic sources for comprehensive understanding

## Disclaimer

This tool was generated with the assistance of Cursor.AI for user ajlennon (Alex J Lennon, ajlennon@dynamicdevices.co.uk).

The analysis is based on publicly available documents from the Harvard Law School Library's Nuremberg Trials Project. Users should verify all claims by consulting original documents and additional academic sources.

## License

GPL-3.0-or-later

