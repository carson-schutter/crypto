# Crypto Sentiment Trading Bot

A Python-based trading bot that analyzes cryptocurrency market sentiment from Reddit and correlates it with live price data from Coinbase Pro to execute automated buy/sell decisions.

## Overview

This project combines social sentiment analysis with real-time market data to create a trading signal. It scrapes top cryptocurrency subreddits to gauge investor sentiment and fetches live price data for Litecoin (LTC) and Bitcoin (BTC). The bot executes trades based on a custom logic that weighs sentiment scores against current asset prices.

### Key Features
* **Sentiment Analysis:** Scrapes Reddit (r/Bitcoin, r/ethereum, r/CryptoCurrency, etc.) using the PRAW API.
* **Fuzzy Logic:** Uses `fuzzywuzzy` to classify post titles as positive, negative, or neutral based on keyword matching.
* **Market Data Integration:** Fetches real-time price data from the Coinbase Pro API.
* **Automated Trading Logic:** Executes buy/sell orders when specific price and sentiment thresholds are met.
* **Transaction Logging:** Records all trades and account states to a local log file (`account_log.txt`).

## Logic & Strategy

The bot calculates an **Investor Sentiment Score** based on:
1.  **Volume:** Post volume over the last 24h, 3 months, and 6 months.
2.  **Sentiment:** Frequency of positive vs. negative phrases in the last 24 hours.

**Trading Rules:**
* **BUY Signal:** If `LTC Price > $70.63` AND `Investor Sentiment > 150`.
* **SELL Signal:** Otherwise (default action).

## Prerequisites

* Python 3.x
* Reddit API Credentials (Client ID, Client Secret, User Agent)
* Coinbase Pro API Credentials (API Key, Secret, Passphrase)# Crypto Sentiment Trading Bot

A Python-based trading bot that analyzes cryptocurrency market sentiment from Reddit and correlates it with live price data from Coinbase Pro to execute automated buy/sell decisions.

## Overview

This project combines social sentiment analysis with real-time market data to create a trading signal. It scrapes top cryptocurrency subreddits to gauge investor sentiment and fetches live price data for Litecoin (LTC) and Bitcoin (BTC). The bot executes trades based on a custom logic that weighs sentiment scores against current asset prices.

### Key Features
* **Sentiment Analysis:** Scrapes Reddit (r/Bitcoin, r/ethereum, r/CryptoCurrency, etc.) using the PRAW API.
* **Fuzzy Logic:** Uses `fuzzywuzzy` to classify post titles as positive, negative, or neutral based on keyword matching.
* **Market Data Integration:** Fetches real-time price data from the Coinbase Pro API.
* **Automated Trading Logic:** Executes buy/sell orders when specific price and sentiment thresholds are met.
* **Transaction Logging:** Records all trades and account states to a local log file (`account_log.txt`).

## Logic & Strategy

The bot calculates an **Investor Sentiment Score** based on:
1.  **Volume:** Post volume over the last 24h, 3 months, and 6 months.
2.  **Sentiment:** Frequency of positive vs. negative phrases in the last 24 hours.

**Trading Rules:**
* **BUY Signal:** If `LTC Price > $70.63` AND `Investor Sentiment > 150`.
* **SELL Signal:** Otherwise (default action).

## Prerequisites

* Python 3.x
* Reddit API Credentials (Client ID, Client Secret, User Agent)
* Coinbase Pro API Credentials (API Key, Secret, Passphrase)
