import pandas as pd


def validate_data(path="data/processed/weekly_processed.parquet"):
    df = pd.read_parquet(path)

    print("===== BASIC INFO =====")
    print(df.info())

    print("\n===== HEAD =====")
    print(df.head())

    print("\n===== TAIL =====")
    print(df.tail())

    print("\n===== MISSING VALUES =====")
    print(df.isna().sum())

    print("\n===== DATE FREQUENCY CHECK =====")
    print(df.index.to_series().diff().value_counts().head())

    print("\n===== BASIC STATS =====")
    print(df[["log_HDFC", "log_BANK_INDEX"]].describe())


if __name__ == "__main__":
    validate_data()
