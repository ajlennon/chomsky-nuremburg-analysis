# CI Deployment Fixes

## Issues Found

### 1. Permission Error ❌
**Error:** `Permission to ajlennon/chomsky-nuremburg-analysis.git denied to github-actions[bot]`

**Root Cause:** The workflow lacked necessary permissions for GitHub Pages deployment.

**Fix Applied:**
- Added `pages: write` permission
- Added `id-token: write` permission (required for GitHub Pages)

### 2. Duplicate Gemfile Entries ⚠️
**Warning:** `Your Gemfile lists the gem jekyll-sitemap (~> 1.4) more than once`

**Root Cause:** Gems were listed both at top level and in `jekyll_plugins` group.

**Fix Applied:**
- Removed duplicate entries from top level
- Kept only in `jekyll_plugins` group (correct location)

### 3. File Conflicts ⚠️
**Warning:** Multiple files with same destination path

**Root Cause:** Files exist in both `reports/` and `_reports/` directories, causing Jekyll conflicts.

**Fix Applied:**
- Excluded `reports/` directory from Jekyll processing
- Using only `_reports/` collection (proper Jekyll collection)

### 4. Deployment Configuration
**Improvements:**
- Added `enable_jekyll: false` (site is already built)
- Added `allow_empty_commit: true` (allows redeployment)
- Added `JEKYLL_ENV: production` for build step

## Files Modified

1. **`.github/workflows/jekyll.yml`**
   - Added `pages: write` and `id-token: write` permissions
   - Added environment variable for Jekyll build
   - Improved deployment configuration

2. **`Gemfile`**
   - Removed duplicate gem entries
   - Kept gems only in `jekyll_plugins` group

3. **`_config.yml`**
   - Excluded `reports/` directory to avoid conflicts
   - Using `_reports/` collection only

## Next Steps

1. **Commit and push changes:**
   ```bash
   git add .github/workflows/jekyll.yml Gemfile _config.yml CI_FIXES.md
   git commit -m "Fix CI deployment: add permissions, fix Gemfile duplicates, resolve file conflicts"
   git push
   ```

2. **Verify deployment:**
   - Check GitHub Actions: https://github.com/ajlennon/chomsky-nuremburg-analysis/actions
   - Should see successful build and deployment

3. **Enable GitHub Pages (if not already):**
   - Go to: https://github.com/ajlennon/chomsky-nuremburg-analysis/settings/pages
   - Source: **GitHub Actions**
   - Save

## Expected Result

After these fixes:
- ✅ Build should complete successfully
- ✅ Deployment should have proper permissions
- ✅ No duplicate gem warnings
- ✅ No file conflict warnings
- ✅ Site should deploy to GitHub Pages

---

**Date:** November 21, 2025

