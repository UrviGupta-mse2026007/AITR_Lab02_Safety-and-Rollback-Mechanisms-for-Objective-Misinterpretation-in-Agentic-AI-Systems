"""Generate test-partition comparison figures from reproduced results."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
METRICS = [
    ("mean_residual_harm", "Mean residual harm", "Lower is better", "mean_residual_harm"),
    ("intervention_rate", "Intervention rate", "Lower is not always better", "intervention_rate"),
    ("false_positive_rate", "False-positive rate", "Lower is better", "false_positive_rate"),
]


def main():
    source = ROOT / "results" / "reproduced" / "all_results.csv"
    if not source.exists():
        raise FileNotFoundError("Run scripts/run_experiment.py first")
    df = pd.read_csv(source)
    test = df[df["partition"] == "test"].copy()
    if test.empty:
        raise ValueError("No test rows in reproduced results")
    out = ROOT / "results" / "figures"
    out.mkdir(parents=True, exist_ok=True)
    for key, title, direction, filename in METRICS:
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.bar(test["policy"], test[key])
        ax.set_title(f"{title} (test partition)")
        ax.set_ylabel(title)
        ax.tick_params(axis="x", rotation=20)
        fig.tight_layout()
        fig.savefig(out / f"{filename}.png", dpi=300)
        fig.savefig(out / f"{filename}.pdf")
        plt.close(fig)
    print(f"Saved figures to {out}")

if __name__ == "__main__":
    main()
