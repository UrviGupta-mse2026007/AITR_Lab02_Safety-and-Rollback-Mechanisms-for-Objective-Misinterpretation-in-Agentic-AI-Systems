"""Re-evaluate the three policies using the saved development-selected thresholds.

This is an evaluation reproduction script. It does not re-run threshold search.
"""
from pathlib import Path
import json
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from evaluation import evaluate_policy

POLICIES = [
    ("fixed_threshold_with_rollback", 0.50),
    ("fixed_threshold_without_rollback", 0.50),
    ("risk_aware_with_rollback", 0.10),
]
PARTITIONS = ["development", "validation", "test"]


def main():
    out = ROOT / "results" / "reproduced"
    out.mkdir(parents=True, exist_ok=True)
    summaries, predictions = [], []
    for partition in PARTITIONS:
        df = pd.read_csv(ROOT / "data" / "splits" / f"{partition}.csv")
        for policy, threshold in POLICIES:
            summary, pred = evaluate_policy(df, policy, threshold, recovery_fraction=0.80)
            summary["partition"] = partition
            pred["partition"] = partition
            summaries.append(summary)
            predictions.append(pred)
    pd.DataFrame(summaries).to_csv(out / "all_results.csv", index=False)
    pd.concat(predictions, ignore_index=True).to_csv(out / "all_predictions.csv", index=False)
    print(pd.DataFrame(summaries).to_string(index=False))
    print(f"Saved outputs to {out}")

if __name__ == "__main__":
    main()
