# A Regime-Aware Multi-Strategy Quantitative Framework for Indian Equities

This project explores how different quantitative trading strategies behave under varying market regimes. Instead of assuming that a strategy works consistently over time, the framework focuses on identifying when a strategy is statistically valid and when it should be avoided.

## Motivation

Most quantitative strategies are presented with the assumption that they work uniformly across time. In practice, financial markets evolve through different regimes, and strategies often fail when their underlying assumptions break. This project is motivated by the idea that understanding when a strategy works is more important than optimizing performance during favorable periods.

## Core Ideas

- Financial markets are non-stationary
- Strategy performance is regime-dependent
- Failure analysis provides more insight than static backtests

## Modules

- Regime-Aware Mean Reversion (in progress)
- Momentum / Trend Following (planned)
- Volatility Regime Analysis (planned)
- Cross-Sectional Signals (planned)

## Current Focus

The current implementation extends a pairs trading strategy by conditioning mean-reversion signals on rolling stationarity regimes, aiming to improve robustness in real-world market conditions.
