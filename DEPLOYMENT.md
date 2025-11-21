# Deployment Guide

## Quick Start

### 1. Install Dependencies

```bash
bundle install
```

### 2. Test Locally

```bash
bundle exec jekyll serve
```

Visit `http://localhost:4000` to preview the site.

### 3. Deploy to GitHub Pages

#### Option A: Automatic (GitHub Actions)

1. Push to GitHub:
```bash
git add .
git commit -m "Initial Jekyll site setup"
git push -u origin main
```

2. Enable GitHub Pages:
   - Go to repository Settings → Pages
   - Source: GitHub Actions
   - The workflow will build and deploy automatically

3. Site will be available at:
   `https://ajlennon.github.io/chomsky-nuremburg-analysis/`

#### Option B: Manual Build

```bash
# Build the site
bundle exec jekyll build

# The _site/ directory contains the static site
# Can be deployed to any static hosting service
```

## Configuration

### Update Base URL

If your repository name is different, update `_config.yml`:

```yaml
baseurl: "/your-repo-name"
```

### Custom Domain (Optional)

1. Add `CNAME` file to root:
```
yourdomain.com
```

2. Update `_config.yml`:
```yaml
url: "https://yourdomain.com"
baseurl: ""
```

## Troubleshooting

### Jekyll Build Errors

- Check Ruby version: `ruby --version` (should be 3.1+)
- Update dependencies: `bundle update`
- Clear cache: `rm -rf .jekyll-cache _site`

### GitHub Pages Not Updating

- Check GitHub Actions workflow status
- Verify `baseurl` matches repository name
- Ensure `main` branch is set as default

### Large Files

The JSON report (7.8 MB) may slow builds. Consider:
- Excluding from Jekyll: Add to `exclude` in `_config.yml`
- Using Git LFS for large files
- Hosting large files separately

## File Structure for Deployment

```
├── _config.yml          # ✅ Required
├── _layouts/            # ✅ Required
├── _includes/           # ✅ Required
├── _reports/            # ✅ Required (reports collection)
├── assets/              # ✅ Required (CSS/JS)
├── index.html           # ✅ Required (homepage)
├── about.md             # ✅ Required
├── analysis.md          # ✅ Required
├── reports.md           # ✅ Required
├── Gemfile              # ✅ Required
└── .github/workflows/   # ✅ Required (CI/CD)
```

## Notes

- Reports are in `_reports/` collection (Jekyll will process them)
- Original `reports/` directory kept for reference
- Python tool in `nuremberg_analysis/` excluded from Jekyll
- Large JSON file included but may slow builds

