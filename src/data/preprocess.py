import pandas as pd
import numpy as np
from pathlib import Path


def preprocess_prices(path="data/raw/weekly_prices.csv"):
    df = pd.read_csv(path, index_col=0, parse_dates=True)

    df.columns = ["HDFC", "BANK_INDEX"]

    # Log-price transformation
    log_df = np.log(df)

    processed = pd.concat([df, log_df.add_prefix("log_")], axis=1)

    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)

    processed.to_parquet(processed_dir / "weekly_processed.parquet")

    print("Preprocessed data saved.")
    return processed


if __name__ == "__main__":
    preprocess_prices()
