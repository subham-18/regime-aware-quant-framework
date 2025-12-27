# A Regime-Aware Relative Value Framework for Indian Banking Equities
# Overview

This project studies how relative value relationships between a single stock and its sector index evolve across different market regimes. Instead of assuming that statistical relationships remain stable over time, the framework explicitly tests when these relationships are valid and avoids trading during unstable periods.

The objective is not to maximize short-term profitability, but to demonstrate a disciplined, assumption-aware approach to quantitative research.

# Motivation

Most retail and academic quantitative strategies implicitly assume stationarity and continuous tradability. In real financial markets, however, structural breaks, macroeconomic shifts, and regime changes frequently invalidate these assumptions.

This project is motivated by the idea that understanding when not to trade is more important than forcing trades at all times. A strategy that stays inactive during unstable regimes is often more robust than one that appears profitable in backtests but fails during regime shifts.

# Core Research Questions

How can we model relative value between a stock and its sector index in a statistically interpretable way?

Does the relative value relationship remain stable over time?

Can we detect periods where mean-reversion assumptions break down?

How selective should signals be to avoid noise-driven trading?

# Methodology
1. Data & Assumptions

Weekly adjusted close prices are used to reduce microstructure noise.

Log-price transformations are applied to ensure additive relationships.

HDFC Bank is modeled relative to the NIFTY Bank Index to capture sector-adjusted behavior.

2. Relative Value Modeling

Ordinary Least Squares (OLS) regression is used to explain stock behavior using the sector index.

The regression residual is interpreted as a sector-neutral relative value spread.

3. Regime Detection

Rolling Augmented Dickey–Fuller (ADF) tests are applied to the spread.

Stationarity is treated as a time-varying property, not a global assumption.

Mean-reversion is only considered valid during statistically stable regimes.

4. Signal Construction

Spread deviations are standardized using rolling Z-scores.

Entry and exit thresholds are chosen conservatively to avoid overtrading.

Signals are explicitly gated by regime validity.

5. Evaluation & Failure Analysis

Signal frequency, inactivity periods, and regime alignment are analyzed.

The framework intentionally accepts long inactive periods as a feature, not a flaw.

Failure during regime transitions is treated as expected behavior rather than model error.

# Key Observations

Stationary regimes are rare and short-lived, reflecting real market behavior.

High inactivity ratios indicate disciplined risk management rather than lack of opportunity.

The framework prioritizes robustness and assumption validity over aggressive optimization.

# Limitations & Extensions

The analysis focuses on a single stock-index pair.

No transaction cost modeling or PnL optimization is performed.

Future extensions may include multiple assets, alternative regime definitions, and portfolio-level analysis.

# Conclusion

This project demonstrates a research-driven approach to statistical arbitrage that emphasizes regime awareness, disciplined inactivity, and failure analysis. Rather than presenting a trading system, it provides a framework for evaluating when quantitative assumptions are valid in real-world markets.