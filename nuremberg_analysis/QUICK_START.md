# Quick Start Guide

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

Required packages:
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `lxml` - XML/HTML parser (faster than default)

## First Run

### Test with a Single Claim

Start with a focused test on one claim to verify everything works:

```bash
python3 -m nuremberg_analysis.main --focus-claims pal_001 --format markdown
```

This will:
1. Extract claim `pal_001` (about Justice Pal being an independent Asian justice)
2. Search the Harvard website for relevant documents
3. Verify the claim
4. Generate a Markdown report

### Run Full Analysis

Once you've verified it works, run the full analysis:

```bash
python3 -m nuremberg_analysis.main
```

This will analyze all 20 claims and generate comprehensive reports.

## Understanding the Output

### Report Structure

Reports are saved in `./reports/` directory with timestamps:

```
reports/
├── chomsky_verification_report_20250115_143022.md
├── chomsky_verification_report_20250115_143022.html
└── chomsky_verification_report_20250115_143022.json
```

### Verification Statuses

- ✅ **Verified**: Strong evidence supports the claim
- ⚠️ **Partially Verified**: Some evidence supports, but mixed or incomplete
- ❌ **Contradicted**: Evidence contradicts the claim
- ❓ **Insufficient Evidence**: Not enough evidence found to verify
- 🔍 **Not Found**: No relevant documents found

### Confidence Levels

Confidence scores range from 0% to 100%:
- **High (70-100%)**: Strong evidence, multiple sources
- **Medium (40-69%)**: Some evidence, may need verification
- **Low (0-39%)**: Weak or conflicting evidence

## Common Issues

### Website Access Issues

If you get connection errors:
- Check your internet connection
- The Harvard website may be temporarily unavailable
- Try increasing `--rate-limit` to 2.0 or higher

### No Documents Found

If few or no documents are found:
- The website structure may have changed (scraper may need updates)
- Some documents may require special access
- Try searching manually on the Harvard website first

### Import Errors

If you get import errors:
```bash
# Make sure you're in the project root
cd /path/to/mcp-remote-testing

# Install dependencies
pip install -r requirements.txt

# Try importing
python3 -c "from nuremberg_analysis import chomsky_claims; print('OK')"
```

## Next Steps

1. **Review Reports**: Check the generated reports for verification results
2. **Manual Verification**: For important claims, manually review original documents
3. **External Sources**: Some claims (e.g., Telford Taylor's book) require external sources
4. **Refinement**: Update claim keywords or verification logic based on results

## Example Workflow

```bash
# 1. Test with one claim
python3 -m nuremberg_analysis.main --focus-claims pal_004 --format markdown

# 2. Review the report
cat reports/chomsky_verification_report_*.md

# 3. If it works, run full analysis
python3 -m nuremberg_analysis.main --rate-limit 1.5

# 4. Review comprehensive report
open reports/chomsky_verification_report_*.html
```

## Tips

- **Start Small**: Test with `--focus-claims` first
- **Use Caching**: Documents are cached - subsequent runs are faster
- **Check Logs**: The tool provides detailed logging of its progress
- **Rate Limiting**: Be respectful - default 1 second is good, increase if needed
- **Multiple Formats**: Use `--format all` to get Markdown, HTML, and JSON

## Getting Help

If you encounter issues:
1. Check the logs for error messages
2. Review `README.md` for detailed documentation
3. Check `USAGE_EXAMPLES.md` for more examples
4. Verify the Harvard website is accessible: https://nuremberg.law.harvard.edu/

