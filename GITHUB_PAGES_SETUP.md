# GitHub Pages Setup Instructions

## ✅ Repository Metadata Configured

The repository has been configured with:
- **Description**: Verification of Noam Chomsky's essay 'If the Nuremberg Laws were Applied...' against Harvard Law School Library's Nuremberg Trials Project documents
- **Homepage**: https://ajlennon.github.io/chomsky-nuremburg-analysis
- **Topics**: chomsky, nuremberg-trials, historical-analysis, document-verification, jekyll, github-pages, war-crimes, international-law, academic-research

## 🔧 Enable GitHub Pages

### Option 1: Via GitHub Web Interface (Recommended)

1. Go to: https://github.com/ajlennon/chomsky-nuremburg-analysis/settings/pages
2. Under "Source", select:
   - **Source**: `GitHub Actions`
3. Click **Save**
4. The site will be automatically deployed when the workflow completes

### Option 2: Via GitHub CLI

```bash
# Check if Pages is enabled
gh api repos/ajlennon/chomsky-nuremburg-analysis/pages

# If not enabled, you may need to enable it via web interface first
# Then configure it to use GitHub Actions
```

## 📊 Check Deployment Status

### Check Workflow Status
```bash
gh run list --limit 5
gh run view <run-id> --log
```

### Check Pages Status
```bash
gh api repos/ajlennon/chomsky-nuremburg-analysis/pages
```

### View Site
Once deployed, visit: https://ajlennon.github.io/chomsky-nuremburg-analysis

## 🔍 Verify Deployment

1. **Check Actions Tab**: https://github.com/ajlennon/chomsky-nuremburg-analysis/actions
   - Should show "Jekyll site CI" workflow running/completed
   - Look for "Deploy to GitHub Pages" step

2. **Check Pages Settings**: https://github.com/ajlennon/chomsky-nuremburg-analysis/settings/pages
   - Source should be "GitHub Actions"
   - Should show deployment status

3. **Check gh-pages Branch**: The workflow creates a `gh-pages` branch automatically
   ```bash
   git fetch origin gh-pages
   git branch -r | grep gh-pages
   ```

## 🐛 Troubleshooting

### Workflow Fails
- Check workflow logs: `gh run view <run-id> --log`
- Verify Gemfile is correct
- Check Ruby version compatibility

### Pages Not Updating
- Ensure workflow completed successfully
- Check Pages settings source is "GitHub Actions"
- Wait a few minutes for propagation

### Site Not Accessible
- Verify baseurl in `_config.yml` matches repository name
- Check repository is public (required for free GitHub Pages)
- Wait 5-10 minutes after first deployment

## 📝 SEO Metadata

The repository includes:
- ✅ Comprehensive description
- ✅ Relevant topics/tags
- ✅ Homepage URL set
- ✅ Proper meta tags in HTML (via Jekyll)
- ✅ Sitemap (via jekyll-sitemap plugin)
- ✅ RSS feed (via jekyll-feed plugin)

## 🚀 Next Steps

1. Wait for workflow to complete (check Actions tab)
2. Enable Pages via Settings → Pages → Source: GitHub Actions
3. Verify site is accessible at: https://ajlennon.github.io/chomsky-nuremburg-analysis
4. Share the site!

