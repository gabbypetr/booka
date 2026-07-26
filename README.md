# Browser Extension Inventory

Browser Extension Inventory scans installed Chromium-based browser extensions and evaluates their requested permissions.

The project reads local extension manifests and generates a simple security report.

## Features

- Chrome
- Edge
- Brave
- Opera
- Permission analysis
- Risk scoring
- JSON report

## Run

```bash
python src/main.py
```

Example output

```
Browser   Name             Risk
Chrome    uBlock Origin    Low
Edge      Grammarly        Medium
Chrome    Unknown Ext      High
```

Future improvements

- Firefox support
- HTML report
- CSV export
- Digital signature validation
