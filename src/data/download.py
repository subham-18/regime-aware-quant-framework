import yfinance as yf
import pandas as pd
from pathlib import Path


def download_weekly_data(tickers, start="2015-01-01", end=None):
    data = yf.download(
        tickers=tickers, start=start, end=end, interval="1wk", auto_adjust=True
    )

    prices = data["Close"]
    prices.dropna(inplace=True)

    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)

    prices.to_csv(raw_dir / "weekly_prices.csv")
    print("Weekly data downloaded and saved.")

    return prices


if __name__ == "__main__":
    tickers = ["HDFCBANK.NS", "^NSEBANK"]
    download_weekly_data(tickers)
