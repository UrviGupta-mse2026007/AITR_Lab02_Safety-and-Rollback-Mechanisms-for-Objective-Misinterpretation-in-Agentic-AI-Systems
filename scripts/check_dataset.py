"""Validate the benchmark CSV files and split integrity."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SPLITS = ROOT / "data" / "splits"
REQUIRED = {"episode_id", "impact", "uncertainty", "reversibility", "harmful_outcome", "template_id", "split"}
EXPECTED = {"development": 360, "validation": 120, "test": 120}


def main():
    frames = {}
    for name, expected_n in EXPECTED.items():
        path = SPLITS / f"{name}.csv"
        if not path.exists():
            raise FileNotFoundError(path)
        df = pd.read_csv(path)
        missing = REQUIRED - set(df.columns)
        if missing:
            raise ValueError(f"{name}: missing columns {sorted(missing)}")
        if len(df) != expected_n:
            raise ValueError(f"{name}: expected {expected_n} rows, found {len(df)}")
        if df["episode_id"].duplicated().any():
            raise ValueError(f"{name}: duplicate episode_id")
        for col in ("impact", "uncertainty", "reversibility"):
            values = pd.to_numeric(df[col], errors="coerce")
            if values.isna().any() or ((values < 0) | (values > 1)).any():
                raise ValueError(f"{name}: {col} must be finite and in [0, 1]")
        if not set(df["harmful_outcome"].unique()).issubset({0, 1}):
            raise ValueError(f"{name}: harmful_outcome must be binary 0/1")
        if set(df["split"].unique()) != {name}:
            raise ValueError(f"{name}: split column does not match filename")
        frames[name] = df
    all_ids = pd.concat([x["episode_id"] for x in frames.values()], ignore_index=True)
    if all_ids.duplicated().any():
        raise ValueError("episode_id overlap across partitions")
    template_sets = {name: set(df["template_id"]) for name, df in frames.items()}
    names = list(template_sets)
    for i, left in enumerate(names):
        for right in names[i + 1:]:
            overlap = template_sets[left] & template_sets[right]
            if overlap:
                raise ValueError(f"template leakage between {left} and {right}: {sorted(overlap)}")
    print("Dataset checks passed.")
    print("Rows:", {k: len(v) for k, v in frames.items()})
    print("Unique episodes:", len(all_ids))
    print("Template overlap: none")

if __name__ == "__main__":
    main()
