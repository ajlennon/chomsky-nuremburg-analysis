# GitHub Pages Setup Instructions

## Issue: Site Not Found After Successful Workflow

If the workflow runs successfully but the site isn't accessible, follow these steps:

## Step 1: Enable GitHub Pages in Repository Settings

1. Go to your repository on GitHub: `https://github.com/ajlennon/chomsky-nuremburg-analysis`
2. Click **Settings** (top right)
3. Scroll down to **Pages** in the left sidebar
4. Under **Source**, select **GitHub Actions** (NOT "Deploy from a branch")
5. Click **Save**

## Step 2: Verify Workflow Completed

1. Go to the **Actions** tab
2. Check that the latest workflow run completed successfully
3. Look for a green checkmark ✓

## Step 3: Check Deployment

1. In the **Actions** tab, click on the latest workflow run
2. Expand the **Deploy to GitHub Pages** step
3. Look for the deployment URL - it should show: `https://ajlennon.github.io/chomsky-nuremburg-analysis/`

## Step 4: Wait for Propagation

- After enabling GitHub Actions as the source, wait 1-2 minutes
- GitHub Pages may take a few minutes to become accessible
- Try accessing: `https://ajlennon.github.io/chomsky-nuremburg-analysis/`

## Step 5: Clear Browser Cache

If the site still doesn't load:
- Clear browser cache
- Try incognito/private mode
- Try a different browser

## Troubleshooting

### If Pages Still Shows 404:

1. **Check Repository Name**: Ensure it matches `chomsky-nuremburg-analysis` (note: "nuremburg" not "nuremberg")
2. **Check Base URL**: In `_config.yml`, `baseurl: "/chomsky-nuremburg-analysis"` must match repository name
3. **Check Workflow Logs**: Look for any errors in the Actions tab
4. **Verify Index File**: Ensure `index.html` exists in `_site/` after build

### Common Issues:

- **Source Not Set**: Must be set to "GitHub Actions" not "Deploy from a branch"
- **Wrong Branch**: Workflow only deploys from `main` branch
- **Build Errors**: Check Actions tab for build failures
- **Permissions**: Ensure workflow has `pages: write` permission (already configured)

## Updated Workflow

The workflow has been updated to use the official `actions/deploy-pages` action which is the recommended approach for GitHub Pages.

## After Enabling GitHub Actions Source

Once you enable "GitHub Actions" as the source in Settings > Pages:
1. The next push will trigger deployment
2. Or manually trigger via Actions > "Jekyll site CI" > Run workflow

---

**Most Common Fix**: Enable "GitHub Actions" as the source in Settings > Pages!

