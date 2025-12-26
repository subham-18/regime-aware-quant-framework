import pandas as pd
from statsmodels.tsa.stattools import adfuller
from pathlib import Path


def rolling_adf(
    path="data/processed/with_spread.parquet",
    window=52,  # 1 year of weekly data
    alpha=0.05,
):
    df = pd.read_parquet(path)
    spread = df["spread"]

    p_values = []

    for i in range(len(spread)):
        if i < window:
            p_values.append(None)
        else:
            window_series = spread.iloc[i - window : i]
            pval = adfuller(window_series)[1]
            p_values.append(pval)

    df["adf_pvalue"] = p_values
    df["stationary_regime"] = df["adf_pvalue"] < alpha

    out_path = Path("data/processed")
    df.to_parquet(out_path / "with_regime.parquet")

    print("Rolling ADF regime detection completed.")

    return df


if __name__ == "__main__":
    rolling_adf()

