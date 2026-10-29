
#!/usr/bin/env python3
"""Summarize the fictional cybersecurity asset inventory."""

import csv
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = PROJECT_ROOT / "data" / "sample_asset_inventory.csv"


def main():
    with CSV_PATH.open(newline="", encoding="utf-8") as file:
        assets = list(csv.DictReader(file))

    if not assets:
        print("No asset records found.")
        return

    counts = Counter(
        row.get("preliminary_risk", "Unrated")
        for row in assets
    )

    print("Cybersecurity OSINT Asset Inventory")
    print("=" * 40)
    print(f"Fictional assets reviewed: {len(assets)}")

    print("\nRisk-level counts:")
    for level in ("High", "Medium", "Low", "Unrated"):
        print(f"  {level}: {counts.get(level, 0)}")

    print("\nItems requiring follow-up:")
    for row in assets:
        if row.get("preliminary_risk") in (
            "High", "Medium", "Unrated"
        ):
            print(
                f"- {row['asset_id']} | "
                f"{row['fictional_hostname']} | "
                f"{row['preliminary_risk']}: "
                f"{row['recommended_action']}"
            )

    print("\nNote: These are fictional training records.")
    print("Risk ratings are illustrative, not proof of vulnerabilities.")


if __name__ == "__main__":
    main()
