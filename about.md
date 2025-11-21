---
layout: page
title: About
permalink: /about/
---

## Project Overview

This project analyzes and verifies claims made in Noam Chomsky's essay "If the Nuremberg Laws were Applied..." against documents from the Harvard Law School Library's Nuremberg Trials Project.

**Scope:** This analysis focuses exclusively on **Nuremberg Trials claims**. Tokyo Trials claims are **out of scope** and are not reviewed in this work.

## Methodology

### Claim Extraction
- Claims extracted and structured from Chomsky's essay
- 20 distinct claims identified across 8 categories
- Each claim includes keywords, context, and expected document types

### Document Search
- Automated web scraping of Harvard's Nuremberg Trials Project website
- Rate-limited requests to respect server resources
- Document caching for offline analysis
- Specialized search functions for specific claims

### Verification Process
- Documents searched for relevance to each claim
- Evidence excerpts extracted (supporting and contradicting)
- Confidence scoring based on evidence strength
- Status determination: Verified, Partially Verified, Contradicted, or Not Found

### Source Verification
- All URLs tested and confirmed accessible
- 110 unique base URLs verified
- No hallucinations - only verified sources cited
- Complete citation list maintained

## Results Summary

- **Total Claims Analyzed:** 20
- **Verified:** 11 claims (55%)
- **Not Found:** 9 claims (45%)
- **Contradicted:** 0 claims (0%)
- **Average Confidence:** 54.0%

## Scope and Limitations

### Scope
- **In Scope:** Claims relating to the Nuremberg Trials (IMT and NMT trials)
- **Out of Scope:** Claims relating to Tokyo Trials (IMTFE) - these are not reviewed in this analysis

### Limitations

1. **Collection Scope:** The Harvard Law School Library's Nuremberg Trials Project collection is **Nuremberg-only** - it does not contain Tokyo Trials documents. This analysis therefore focuses exclusively on Nuremberg Trials claims.
2. **External Sources:** Some claims require external sources (e.g., Telford Taylor's "Nuremberg and Vietnam")
3. **Automated Analysis:** This is an automated tool - full verification may require manual review

## Source

**Primary Source:** [Harvard Law School Library's Nuremberg Trials Project](https://nuremberg.law.harvard.edu/)

The Harvard collection includes:
- Trial transcripts (IMT and NMT trials)
- Document books and exhibits
- Evidence files
- Photographs
- Searchable full-text versions

## Analysis Tool

The project includes a comprehensive Python analysis tool located in `nuremberg_analysis/`:

- `chomsky_claims.py` - Claim extraction and structuring
- `document_scraper.py` - Web scraper for Harvard website
- `claim_verifier.py` - Verification logic
- `report_generator.py` - Report generation
- `main.py` - Command-line interface

See the [Analysis](/analysis) page for usage instructions.

## Contact

**Author:** Alex J Lennon  
**Email:** ajlennon@dynamicdevices.co.uk  
**Analysis Date:** November 20, 2025

## Disclaimer

This analysis is based on publicly available documents from the Harvard Law School Library's Nuremberg Trials Project. Users should verify all claims by consulting original documents and additional academic sources.

The tool analyzes historical documents related to war crimes trials. Documents may contain graphic descriptions of violence and genocide. The tool should be used responsibly, and automated analysis has limitations.

