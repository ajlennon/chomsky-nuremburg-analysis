# Chomsky Nuremberg Analysis

Verification of Noam Chomsky's essay "If the Nuremberg Laws were Applied..." against documents from the Harvard Law School Library's Nuremberg Trials Project.

## Website

This project includes a Jekyll static website. To view locally:

```bash
# Install dependencies
bundle install

# Run Jekyll server
bundle exec jekyll serve

# Visit http://localhost:4000
```

## Project Structure

```
├── _config.yml              # Jekyll configuration
├── _layouts/                # Jekyll layouts
├── _includes/               # Jekyll includes (header, footer)
├── _reports/                # Report collection (Jekyll)
├── assets/                  # CSS and JavaScript
├── nuremberg_analysis/      # Python analysis tool
├── reports/                 # Original reports directory
└── index.html               # Homepage
```

## Analysis Tool

The Python analysis tool is located in `nuremberg_analysis/`. See the [Analysis](/analysis) page for usage instructions.

## Key Findings

- **20 claims analyzed**
- **11 verified (55%)**
- **110 source URLs verified**
- **30,000+ evidence excerpts**

## Source

**Primary Source:** [Harvard Law School Library's Nuremberg Trials Project](https://nuremberg.law.harvard.edu/)

## GitHub Pages

This site is configured for GitHub Pages. The `baseurl` in `_config.yml` should match your repository name.

## License

GPL-3.0-or-later
