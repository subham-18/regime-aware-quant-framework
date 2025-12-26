import pandas as pd
from pathlib import Path


def compute_zscore_signals(
    path="data/processed/with_regime.parquet", window=52, entry_z=2.0, exit_z=0.5
):
    df = pd.read_parquet(path)

    # Rolling statistics
    rolling_mean = df["spread"].rolling(window).mean()
    rolling_std = df["spread"].rolling(window).std()

    df["zscore"] = (df["spread"] - rolling_mean) / rolling_std

    # Initialize signal column
    df["signal"] = 0

    # Generate signals ONLY when regime is valid
    df.loc[(df["stationary_regime"]) & (df["zscore"] > entry_z), "signal"] = (
        -1
    )  # Short spread (HDFC rich)

    df.loc[(df["stationary_regime"]) & (df["zscore"] < -entry_z), "signal"] = (
        1  # Long spread (HDFC cheap)
    )

    # Exit condition
    df.loc[(df["stationary_regime"]) & (df["zscore"].abs() < exit_z), "signal"] = 0

    out_path = Path("data/processed")
    df.to_parquet(out_path / "with_signals.parquet")

    print("Z-score signal construction completed.")
    return df


if __name__ == "__main__":
    compute_zscore_signals()
