# A Regime-Aware Relative Value Framework for Indian Banking Equities

This project studies how relative value relationships between a single stock and its sector index behave across different market regimes. Instead of assuming stable statistical relationships, the framework explicitly tests when such relationships are valid and avoids trading during unstable regimes.

## Core Ideas
- Financial markets are non-stationary
- Relative value relationships can break across regimes
- Strategy validity matters more than raw backtest performance
- Failure analysis is as important as success analysis

## Motivation
Most quantitative strategies implicitly assume stable relationships over time. In practice, structural breaks caused by macro events, sector rotations, and index rebalancing often invalidate these assumptions. This project is motivated by the idea that understanding *when not to trade* is critical for robust quantitative systems.

## Current Focus (Module 1)
- Weekly adjusted price data
- HDFC Bank vs NIFTY Bank Index
- Log-price transformations for relative value modeling
- Clean data pipeline with explicit assumptions

Future modules will extend this framework with spread modeling, regime detection, and strategy evaluation.
