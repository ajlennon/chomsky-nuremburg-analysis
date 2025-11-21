# Web Accessibility Guide

All analysis documents are now accessible through the website.

## Document Structure

### Main Pages

1. **Homepage** (`/`)
   - Overview and key findings
   - Quick links to main documents
   - Statistics and summary

2. **Reports Index** (`/reports/`)
   - Complete list of all analysis documents
   - Organized by category and purpose
   - Reading paths for different audiences

3. **About** (`/about/`)
   - Project methodology
   - Sources and limitations
   - Contact information

4. **Analysis Tool** (`/analysis/`)
   - Python tool documentation
   - Usage instructions
   - Command-line options

### Report Documents (in `/reports/` collection)

All documents are accessible at `/reports/[name]/`:

1. **EXECUTIVE_SUMMARY** (`/reports/EXECUTIVE_SUMMARY/`)
   - Plain language overview
   - Best starting point for general readers

2. **GLOSSARY** (`/reports/GLOSSARY/`)
   - Legal and historical terms explained

3. **TIMELINE** (`/reports/TIMELINE/`)
   - Key dates and historical context

4. **WHO_IS_WHO** (`/reports/WHO_IS_WHO/`)
   - Key figures explained

5. **VISUAL_SUMMARY** (`/reports/VISUAL_SUMMARY/`)
   - Charts, graphs, and statistics

6. **ACADEMIC_PAPER** (`/reports/ACADEMIC_PAPER/`)
   - Scholarly format with citations

7. **CHOMSKY_ANNOTATED_VERIFIED** (`/reports/CHOMSKY_ANNOTATED_VERIFIED/`)
   - Complete annotated essay

8. **ANALYSIS_SUMMARY** (`/reports/ANALYSIS_SUMMARY/`)
   - Executive summary of findings

9. **chomsky_verification_report_20251120_202811** (`/reports/chomsky_verification_report_20251120_202811/`)
   - Detailed verification report

10. **verified_urls** (`/reports/verified_urls/`)
    - List of verified source URLs

11. **README** (`/reports/README/`)
    - Reports directory guide

## Navigation

### Header Navigation
- Home
- Analysis
- Reports
- About

### Homepage Quick Links
- Executive Summary (featured)
- Annotated Essay
- Academic Paper
- All Reports

### Supporting Materials Section
- Glossary
- Timeline
- Who's Who
- Visual Summary

## URL Structure

All reports follow Jekyll collection permalink structure:
- Collection: `_reports/`
- Permalink: `/reports/:name/`
- Example: `/reports/EXECUTIVE_SUMMARY/`

## Reading Paths

### Quick Understanding (10 minutes)
1. `/reports/EXECUTIVE_SUMMARY/`
2. `/reports/VISUAL_SUMMARY/`

### Comprehensive Study (2-3 hours)
1. `/reports/EXECUTIVE_SUMMARY/`
2. `/reports/GLOSSARY/` + `/reports/TIMELINE/` + `/reports/WHO_IS_WHO/`
3. `/reports/CHOMSKY_ANNOTATED_VERIFIED/`
4. `/reports/ACADEMIC_PAPER/`

### Academic Research
1. `/reports/ACADEMIC_PAPER/`
2. `/reports/CHOMSKY_ANNOTATED_VERIFIED/`
3. `/reports/verified_urls/`
4. `/reports/chomsky_verification_report_20251120_202811/` (JSON data)

## File Organization

```
_data_drive/personal/chomsky/
├── index.html                    # Homepage
├── reports.md                    # Reports index page
├── about.md                      # About page
├── analysis.md                   # Analysis tool page
├── _reports/                     # Jekyll collection
│   ├── EXECUTIVE_SUMMARY.md
│   ├── GLOSSARY.md
│   ├── TIMELINE.md
│   ├── WHO_IS_WHO.md
│   ├── VISUAL_SUMMARY.md
│   ├── ACADEMIC_PAPER.md
│   ├── CHOMSKY_ANNOTATED_VERIFIED.md
│   ├── ANALYSIS_SUMMARY.md
│   ├── chomsky_verification_report_20251120_202811.md
│   ├── verified_urls.md
│   ├── verified_urls.txt
│   └── README.md
└── _config.yml                   # Jekyll config
```

## Jekyll Configuration

- Collection: `reports` (output: true)
- Permalink: `/reports/:name/`
- Layout: `report` (default for reports)
- Excluded: `reports/` directory (old location)

## Deployment

The site is deployed via GitHub Pages:
- Repository: `ajlennon/chomsky-nuremburg-analysis`
- Branch: `gh-pages` (auto-generated)
- Workflow: `.github/workflows/jekyll.yml`

## Testing

To test locally (requires Ruby/Bundler):
```bash
bundle install
bundle exec jekyll serve
```

Then visit: `http://localhost:4000/chomsky-nuremburg-analysis/`

## All Documents Accessible

✅ All 11 report documents are in `_reports/` collection  
✅ All have proper front matter  
✅ All are accessible via `/reports/[name]/` URLs  
✅ Homepage links to key documents  
✅ Reports index page lists all documents  
✅ Navigation includes Reports link  

---

**All analysis documents are now accessible through the website!**

