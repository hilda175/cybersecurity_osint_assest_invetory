# Cybersecurity OSINT Asset Inventory & Risk Assessment

## Project overview
This beginner-friendly cybersecurity project demonstrates how to document publicly observable information about a **simulated organization**, identify potential exposure, and prioritize defensive follow-up. All records in this repository are fictional training data. No real systems were scanned or tested.

## Objectives
- Organize asset information in a simple inventory.
- Record technology/banner clues and potential risks.
- Apply a consistent, transparent risk-rating method.
- Produce a concise report with recommended defensive actions.
- Practice clear technical documentation.

## Repository contents
- `data/sample_asset_inventory.csv` — fictional sample asset inventory.
- `scripts/analyze_inventory.py` — Python script that summarizes risk levels.
- `reports/sample_findings.md` — example findings and recommendations.
- `methodology.md` — scope, limitations, and ethical approach.

## How to run
Requires Python 3 (no extra packages needed).

```bash
python scripts/analyze_inventory.py
```

The script reads the sample CSV and prints a summary by risk level and the assets that need follow-up.

## Risk-rating approach
This is a simple **training heuristic**, not a formal vulnerability score:
- **High**: exposed service or outdated/unknown component that warrants prompt verification.
- **Medium**: information disclosure or configuration that should be reviewed.
- **Low**: limited concern based on the fictional evidence available.
- **Unrated**: insufficient evidence to assign a rating.

A banner or version string alone does not prove a device is vulnerable. Findings should be validated by an authorized owner using reliable evidence.

## Ethical and legal boundaries
- Use only systems you own or have explicit written permission to assess.
- Do not scan, exploit, access, or attempt to log in to third-party systems.
- Do not collect personal data or sensitive information.
- The sample data is fictional and is included only to demonstrate the workflow.

## Skills demonstrated
Basic Python, CSV data handling, asset inventory, risk triage, defensive recommendations, and technical report writing.

## Next improvements
- Add a severity rationale and evidence field for each finding.
- Add input validation and export results to a report file.
- Test the process with a lab environment you control and document the authorized scope.
