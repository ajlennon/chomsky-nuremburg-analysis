# Project Organization

This document describes the organization of the Chomsky Nuremberg Analysis project, now structured as a Jekyll static website.

## Directory Structure

```
chomsky/
├── _config.yml                    # Jekyll configuration
├── _layouts/                      # Jekyll page layouts
│   ├── default.html              # Base layout
│   ├── page.html                 # Standard page layout
│   └── report.html               # Report layout
├── _includes/                     # Reusable components
│   ├── header.html               # Site header/navigation
│   └── footer.html               # Site footer
├── _reports/                      # Report collection (Jekyll)
│   ├── CHOMSKY_ANNOTATED_VERIFIED.md
│   ├── ANALYSIS_SUMMARY.md
│   ├── chomsky_verification_report_20251120_202811.md
│   ├── chomsky_verification_report_20251120_202811.html
│   ├── chomsky_verification_report_20251120_202811.json
│   └── verified_urls.txt
├── _site/                         # Generated site (gitignored)
├── assets/                        # Static assets
│   ├── css/
│   │   └── main.css              # Main stylesheet
│   └── js/
│       └── main.js               # JavaScript
├── nuremberg_analysis/            # Python analysis tool
│   ├── __init__.py
│   ├── chomsky_claims.py
│   ├── claim_verifier.py
│   ├── document_scraper.py
│   ├── main.py
│   ├── report_generator.py
│   └── test_basic.py
├── reports/                       # Original reports (kept for reference)
├── .github/
│   └── workflows/
│       └── jekyll.yml            # GitHub Actions CI/CD
├── index.html                     # Homepage
├── about.md                       # About page
├── analysis.md                    # Analysis tool documentation
├── reports.md                     # Reports listing page
├── README.md                      # Project README
├── Gemfile                        # Ruby dependencies
└── .gitignore                    # Git ignore rules
```

## Key Changes

### Jekyll Structure
- **Reports moved to `_reports/`**: Reports are now in a Jekyll collection with front matter
- **Layouts created**: Three layouts for different content types
- **Includes**: Header and footer components for consistent navigation
- **Assets**: CSS and JavaScript in `assets/` directory

### Pages Created
1. **Homepage** (`index.html`): Overview with stats and key findings
2. **About** (`about.md`): Project methodology and information
3. **Analysis** (`analysis.md`): Documentation for the Python tool
4. **Reports** (`reports.md`): Listing of available reports

### Styling
- Modern, responsive design
- Color-coded verification status (green for verified)
- Mobile-friendly navigation
- Professional typography

## GitHub Pages Setup

The project is configured for GitHub Pages:

1. **Base URL**: Set in `_config.yml` to match repository name
2. **GitHub Actions**: Automated build and deployment workflow
3. **Branch**: Uses `main` branch (renamed from master)

## Local Development

```bash
# Install Ruby dependencies
bundle install

# Run Jekyll server
bundle exec jekyll serve

# Build site
bundle exec jekyll build
```

## Deployment

### Manual Deployment
```bash
# Build site
bundle exec jekyll build

# The _site/ directory contains the static site
# Can be deployed to any static hosting service
```

### GitHub Pages (Automatic)
- Push to `main` branch
- GitHub Actions will build and deploy automatically
- Site available at: `https://ajlennon.github.io/chomsky-nuremburg-analysis/`

## File Organization Rationale

### Why `_reports/` instead of `reports/`?
- Jekyll collections use underscore prefix
- Allows reports to be processed as Jekyll pages
- Original `reports/` directory kept for reference

### Why separate `assets/`?
- Standard Jekyll convention
- Better organization
- Easier to manage CSS/JS

### Why keep `nuremberg_analysis/`?
- Python tool is still functional
- Can be used to regenerate reports
- Documented on Analysis page

## Next Steps

1. **Review**: Check the site locally with `bundle exec jekyll serve`
2. **Customize**: Update `_config.yml` with your details
3. **Deploy**: Push to GitHub and enable Pages
4. **Update**: Add new reports to `_reports/` directory

## Notes

- Reports in `_reports/` have front matter added for Jekyll
- Original reports remain in `reports/` directory
- Large JSON file (7.8 MB) included but may slow site generation
- Consider excluding very large files from Jekyll processing if needed

