---
layout: page
title: About
permalink: /about/
---

## Background and Motivation

I discovered Chomsky's work decades ago and have long been interested in his academic approach to geopolitics and power. His essay ["If the Nuremberg Laws were Applied..."](https://chomsky.info/1990____-2/) particularly interested me, and I have always wondered how accurate his claims were.

With the recent release of digitized archives and the emergence of AI agentic tools, I wanted to see what we could do in terms of an analysis. This project serves two purposes:

1. **Personal Understanding:** To verify Chomsky's claims against primary source documents
2. **Tool Evaluation:** To explore how well modern AI agentic tools can assist in historical research and claim verification

This analysis represents an experiment in using AI tools to conduct rigorous historical research - testing both the capabilities of these tools and the accuracy of Chomsky's historical claims.

## Project Overview

This project analyzes and verifies claims made in Noam Chomsky's essay ["If the Nuremberg Laws were Applied..."](https://chomsky.info/1990____-2/) (delivered around 1990) against documents from the Harvard Law School Library's Nuremberg Trials Project.

**Why Now?** This analysis is possible because the Harvard Law School Library has recently released a fully digitized and searchable archive of the Nuremberg Trials documents. The library received the bulk of this collection in 1949, digitization began in 1998, and the archive has been recently released as a fully searchable online collection with over 750,000 pages of documents.

**Scope:** This analysis focuses exclusively on **Nuremberg Trials claims**. Tokyo Trials claims are **not reviewed** because there is **no available evidence in the Harvard archive we are using** - the collection contains only Nuremberg Trials documents, not Tokyo Trials materials.

**Note:** Tokyo Trials materials are available in other online archives, including the [Tokyo Trial Database](http://tokyotrial.cn), [University of Wisconsin-Madison Libraries](https://search.library.wisc.edu/database/UWI60168), [Japan Center for Asian Historical Records (JACAR)](https://www.jacar.go.jp/english/), and the [Hoover Institution Library & Archives](https://oac.cdlib.org/findaid/ark:/13030/kt6b69q2rf).

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

**Archive Provenance:**
- The Harvard Law School Library received the bulk of this collection in **1949**, following the conclusion of the trials
- The library has since added documents donated by tribunal participants
- The digitization project began in **1998** to preserve deteriorating documents and enhance accessibility
- The archive has been recently released as a fully searchable online collection

The Harvard collection includes:
- Over 750,000 pages of documents
- Trial transcripts (IMT and NMT trials)
- Document books and exhibits
- Evidence files
- Photographs
- Searchable full-text versions

**Note:** The collection contains only Nuremberg Trials documents - it does not include Tokyo Trials materials, which is why Tokyo Trials claims are not reviewed in this analysis.

## Analysis Tool

The project includes a comprehensive Python analysis tool located in `nuremberg_analysis/`:

- `chomsky_claims.py` - Claim extraction and structuring
- `document_scraper.py` - Web scraper for Harvard website
- `claim_verifier.py` - Verification logic
- `report_generator.py` - Report generation
- `main.py` - Command-line interface
- `tokyo_scraper.py` - Tokyo Trials document scraper
- `tokyo_verifier.py` - Tokyo Trials claim verification
- `tokyo_main.py` - Tokyo Trials analysis script

These tools were developed using AI agentic assistance (Cursor Composer 1) to automate the process of:
- Extracting and structuring claims from Chomsky's essay
- Searching and scraping relevant documents from archives
- Verifying claims against primary source evidence
- Generating comprehensive reports with citations

See the [Analysis](/analysis) page for usage instructions.

## Contact

**Author:** Alex J Lennon <ajlennon@gmail.com>  
**With assistance from:** Cursor Composer 1  
**Analysis Date:** November 20, 2025

## Disclaimer

This analysis is based on publicly available documents from the Harvard Law School Library's Nuremberg Trials Project. Users should verify all claims by consulting original documents and additional academic sources.

The tool analyzes historical documents related to war crimes trials. Documents may contain graphic descriptions of violence and genocide. The tool should be used responsibly, and automated analysis has limitations.

