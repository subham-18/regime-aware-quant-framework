import pandas as pd
import statsmodels.api as sm
from pathlib import Path


def compute_ols_spread(path="data/processed/weekly_processed.parquet"):
    df = pd.read_parquet(path)

    y = df["log_HDFC"]
    X = df["log_BANK_INDEX"]

    X = sm.add_constant(X)  # adds intercept (alpha)

    model = sm.OLS(y, X).fit()

    alpha = model.params["const"]
    beta = model.params["log_BANK_INDEX"]

    # Residual = relative value spread
    df["spread"] = y - (alpha + beta * df["log_BANK_INDEX"])

    out_path = Path("data/processed")
    df.to_parquet(out_path / "with_spread.parquet")

    print("OLS completed")
    print(f"Alpha (α): {alpha}")
    print(f"Beta (β): {beta}")

    return df, model


if __name__ == "__main__":
    compute_ols_spread()
