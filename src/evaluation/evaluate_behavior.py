import pandas as pd


def evaluate_behavior(path="data/processed/with_signals.parquet"):
    df = pd.read_parquet(path)

    print("===== SIGNAL DISTRIBUTION =====")
    print(df["signal"].value_counts())

    print("\n===== SIGNALS BY REGIME =====")
    print(pd.crosstab(df["signal"], df["stationary_regime"], normalize="columns"))

    print("\n===== Z-SCORE STATS DURING SIGNALS =====")
    print(df[df["signal"] != 0]["zscore"].describe())

    print("\n===== HOW OFTEN DO WE STAY INACTIVE =====")
    inactive_ratio = (df["signal"] == 0).mean()
    print(f"Inactive ratio: {inactive_ratio:.2%}")

    return df


if __name__ == "__main__":
    evaluate_behavior()
