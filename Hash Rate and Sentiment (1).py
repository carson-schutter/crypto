#!/usr/bin/env python
# coding: utf-8

# In[69]:


import requests

while True:
    response = requests.get("https://blockchain.info/q/hashrate")
    
    if response.status_code == 200:
        # Print the content of the response
        print(response.json())

    
print(1)
    


# In[24]:


import requests

# The URL from your curl command
url = "https://mempool.space/api/v1/mining/hashrate/1y"

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the content of the response
    print(response.json())
else:
    # Print an error message if something went wrong
    print(f"Failed to retrieve data: {response.status_code}")
    
    


# In[ ]:


int i

while i <= n:
    print(i)
    i = i + 1


# In[55]:


import praw
import datetime
from collections import Counter


print(1)

neutral_phrases = ["cryptocurrency", "bitcoin", "ethereum", "litecoin", "tether usd", "bnb", "binance coin", "btc", "ltc", "solana", "usdc", "robinhood crypto", "binance", "coinbase"]
positive_phrases = ["buy crypto", "crypto summer", "crypto etf", "blockchain etf", "blockchain fund", "crypto fund", "institutional crypto", "institutional blockchain", "to the moon", "crypto bullrun", "buy crypto"]
negative_phrases = ["crypto fraud", "crypto regulations", "crypto etfs", "sell crypto", "crypto winter", "crypto burst", "crypto bubble", "sinking ship", "lost cause"]

from fuzzywuzzy import fuzz  # For fuzzy string matching

# Function to normalize text
def normalize_text(text):
    text = text.lower()
    text = ' '.join(text.split())  # Remove extra spaces
    return text


# Function for fuzzy phrase matching
def fuzzy_phrase_count(text_data, phrase):
    count = 0
    for text in text_data:
        if fuzz.partial_ratio(normalize_text(text), normalize_text(phrase)) > 80:  # 80 is the threshold for a match
            count += 1
    return count

print(2)

# Function to calculate phrase frequency with fuzzy matching
def calculate_phrase_frequency_fuzzy(text_data, phrases):
    total_count = 0
    for phrase in phrases:
        total_count += fuzzy_phrase_count(text_data, phrase)
    return total_count

# Rest of the code remains the same, but replace the calculate_phrase_frequency call with calculate_phrase_frequency_fuzzy


# Setup PRAW with your Reddit API credentials
reddit = praw.Reddit(client_id="XXXX",
                     client_secret="XXXX",
                     user_agent="SurfBot by u/Swimmer")

# List of top 30 cryptocurrency subreddits
subreddits = ['Bitcoin', 'ethereum', 'CryptoCurrency','Litecoin','CryptoMarkets',]  # Add more subreddits

print(3)

# Function to fetch post titles
def fetch_post_titles(subreddit_name, time_filter):
    subreddit = reddit.subreddit(subreddit_name)
    return [submission.title for submission in subreddit.top(time_filter=time_filter, limit=None)]

# Fetch post titles for different time periods
def fetch_data_for_all_subreddits(subreddits, time_filter):
    all_titles = []
    for subreddit_name in subreddits:
        titles = fetch_post_titles(subreddit_name, time_filter)
        all_titles.extend(titles)
    return all_titles

# Fetch data
data_24h = fetch_data_for_all_subreddits(subreddits, 'day')
data_3m = fetch_data_for_all_subreddits(subreddits, 'month')
data_6m = fetch_data_for_all_subreddits(subreddits, 'year')


# Count volume
volume_24h = len(data_24h)
volume_3m = len(data_3m) / 90  # Average per day over 3 months
volume_6m = len(data_6m) / 180  # Average per day over 6 months

print(6)

# Calculate phrase frequencies
positive_count = calculate_phrase_frequency_fuzzy(data_24h, positive_phrases)
negative_count = calculate_phrase_frequency_fuzzy(data_24h, negative_phrases)
neutral_count = calculate_phrase_frequency_fuzzy(data_24h, neutral_phrases)

# Calculate weighted score components
volume_24h_6m = 40 * (len(data_24h) / max(1, len(data_6m)))
volume_24h_3m = 5 * (len(data_24h) / max(1, len(data_3m)))
positive_score = 25 * (positive_count / max(1, len(data_24h)))
negative_score = -20 * (negative_count / max(1, len(data_24h)))
neutral_score = 5 * (neutral_count / max(1, len(data_24h)))



# Calculate final InvestorSentiment score
InvestorSentiment = volume_24h_6m + volume_24h_3m + positive_score + negative_score + neutral_score
InvestorSentiment = max(min(InvestorSentiment, 1000), -1000)



print("Investor Sentiment Score:", InvestorSentiment)


# In[54]:


import praw
from fuzzywuzzy import fuzz  # For fuzzy string matching

# Setup PRAW with your Reddit API credentials
reddit = praw.Reddit(client_id="XXXX",
                     client_secret="XXXX",
                     user_agent="SurfBot by u/Swimmer")

# List of top cryptocurrency subreddits
subreddits = ['Bitcoin', 'ethereum', 'CryptoCurrency']  # Add more subreddits

# Phrases for sentiment analysis
neutral_phrases = ["cryptocurrency", "bitcoin", "ethereum", "litecoin", "tether usd", "bnb", "binance coin", "btc", "ltc", "solana", "usdc", "robinhood crypto", "binance", "coinbase"]
positive_phrases = ["buy crypto", "crypto summer", "crypto etf", "blockchain etf", "blockchain fund", "crypto fund", "institutional crypto", "institutional blockchain", "to the moon", "crypto bullrun", "buy crypto"]
negative_phrases = ["crypto fraud", "crypto regulations", "crypto etfs", "sell crypto", "crypto winter", "crypto burst", "crypto bubble", "sinking ship", "lost cause"]

# Function to normalize text
def normalize_text(text):
    text = text.lower()
    text = ' '.join(text.split())  # Remove extra spaces
    return text

# Function for fuzzy phrase matching
def fuzzy_phrase_count(text_data, phrase):
    count = 0
    for text in text_data:
        if fuzz.partial_ratio(normalize_text(text), normalize_text(phrase)) > 80:  # 80 is the threshold for a match
            count += 1
    return count

# Function to fetch post titles
def fetch_post_titles(subreddit_name, time_filter):
    subreddit = reddit.subreddit(subreddit_name)
    return [submission.title for submission in subreddit.top(time_filter=time_filter, limit=None)]

# Fetch post titles for different time periods
def fetch_data_for_all_subreddits(subreddits, time_filter):
    all_titles = []
    for subreddit_name in subreddits:
        titles = fetch_post_titles(subreddit_name, time_filter)
        all_titles.extend(titles)
    return all_titles

print(6)

# Fetch data
data_24h = fetch_data_for_all_subreddits(subreddits, 'day')
data_3m = fetch_data_for_all_subreddits(subreddits, 'month')
data_6m = fetch_data_for_all_subreddits(subreddits, 'year')

print(7)

# Count volume and calculate phrase frequencies
volume_24h = len(data_24h)
volume_3m = len(data_3m) / 90  # Average per day over 3 months
volume_6m = len(data_6m) / 180  # Average per day over 6 months


positive_count = sum(fuzzy_phrase_count(data_24h, phrase) for phrase in positive_phrases)
negative_count = sum(fuzzy_phrase_count(data_24h, phrase) for phrase in negative_phrases)
neutral_count = sum(fuzzy_phrase_count(data_24h, phrase) for phrase in neutral_phrases)

# Calculate weighted score components
volume_score_24h_6m = 35 * (volume_24h / max(1, volume_6m))
volume_score_24h_3m = 10 * (volume_24h / max(1, volume_3m))
positive_score = 25 * (positive_count / max(1, volume_24h))
negative_score = -25 * (negative_count / max(1, volume_24h))
neutral_score = 25 * (neutral_count / max(1, volume_24h))

# Calculate final InvestorSentiment score
InvestorSentiment = volume_score_24h_6m + volume_score_24h_3m + positive_score + negative_score + neutral_score
InvestorSentiment = max(min(InvestorSentiment, 1000), -1000)

print("Investor Sentiment Score:", InvestorSentiment)


# In[ ]:


# The Following Code Derives an investor sentiment score from Reddit Posts.


# In[60]:


import praw
from fuzzywuzzy import fuzz  # For fuzzy string matching

# Setup PRAW with your Reddit API credentials
reddit = praw.Reddit(client_id="XXXX",
                     client_secret="XXXX",
                     user_agent="SurfBot by u/Swimmer")

# List of top cryptocurrency subreddits
subreddits = ['Bitcoin', 'ethereum', 'CryptoCurrency','CryptoMarkets','Ethereum','btc','BitcoinMarkets']  # Add more subreddits

# Phrases for sentiment analysis
neutral_phrases = ["cryptocurrency", "bitcoin", "ethereum", "litecoin", "tether usd", "bnb", "binance coin", "btc", "ltc", "solana", "usdc", "robinhood crypto", "binance", "coinbase"]
positive_phrases = ["buy","buy crypto", "crypto summer", "crypto etf", "blockchain etf", "blockchain fund", "crypto fund", "institutional crypto", "institutional blockchain", "to the moon", "crypto bullrun", "buy crypto","bull","bull market","bullish",]
negative_phrases = ["sell","HODL","crypto fraud", "crypto regulations", "crypto etfs", "sell crypto", "crypto winter", "crypto burst", "crypto bubble", "sinking ship", "lost cause","sell","HODL","Pump and Dump","Rug Pull"]

# Function to normalize text
def normalize_text(text):
    text = text.lower()
    text = ' '.join(text.split())  # Remove extra spaces
    return text

# Function for fuzzy phrase matching
def fuzzy_phrase_count(text_data, phrase):
    count = 0
    for text in text_data:
        if fuzz.partial_ratio(normalize_text(text), normalize_text(phrase)) > 80:  # 80 is the threshold for a match
            count += 1
    return count

# Function to fetch post titles
def fetch_post_titles(subreddit_name, time_filter):
    subreddit = reddit.subreddit(subreddit_name)
    return [submission.title for submission in subreddit.top(time_filter=time_filter, limit=None)]

# Fetch post titles for different time periods
def fetch_data_for_all_subreddits(subreddits, time_filter):
    all_titles = []
    for subreddit_name in subreddits:
        titles = fetch_post_titles(subreddit_name, time_filter)
        all_titles.extend(titles)
    return all_titles

print(6)

# Fetch data
data_24h = fetch_data_for_all_subreddits(subreddits, 'day')
data_3m = fetch_data_for_all_subreddits(subreddits, 'month')
data_6m = fetch_data_for_all_subreddits(subreddits, 'year')

print(7)

# Count volume and calculate phrase frequencies
volume_24h = len(data_24h)
volume_3m = len(data_3m) / 90  # Average per day over 3 months
volume_6m = len(data_6m) / 180  # Average per day over 6 months


def classify_post(title, positive_phrases, negative_phrases, neutral_phrases):
    title_normalized = normalize_text(title)
    # Check for positive, negative, and neutral phrases
    if any(fuzz.partial_ratio(title_normalized, normalize_text(phrase)) > 80 for phrase in positive_phrases):
        return "positive"
    elif any(fuzz.partial_ratio(title_normalized, normalize_text(phrase)) > 80 for phrase in negative_phrases):
        return "negative"
    elif any(fuzz.partial_ratio(title_normalized, normalize_text(phrase)) > 80 for phrase in neutral_phrases):
        return "neutral"
    else:
        return "neutral"  # Default to neutral if no specific phrases are found

# Count classifications
positive_count, negative_count, neutral_count = 0, 0, 0

for title in data_24h:
    classification = classify_post(title, positive_phrases, negative_phrases, neutral_phrases)
    if classification == "positive":
        positive_count += 1
    elif classification == "negative":
        negative_count += 1
    elif classification == "neutral":
        neutral_count += 1


# Calculate weighted score components
volume_score_24h_6m = 35 * (volume_24h / max(1, volume_6m))
volume_score_24h_3m = 15 * (volume_24h / max(1, volume_3m))
positive_score = 40 * (positive_count / max(1, volume_24h))
negative_score = -40 * (negative_count / max(1, volume_24h))
neutral_score = 10 * (neutral_count / max(1, volume_24h))

print("positive score", positive_score)
print("neg score", negative_score)
print("neut score", neutral_score)

# Calculate final InvestorSentiment score
InvestorSentiment = volume_score_24h_6m + volume_score_24h_3m + positive_score + negative_score + neutral_score
InvestorSentiment = max(min(InvestorSentiment, 1000), -1000)

print("Investor Sentiment Score:", InvestorSentiment)


# In[ ]:


## Different score calc, and I tried to get the code to run faster by only pulling 3 month and 6month every 8 hours.


# In[71]:


import praw
from fuzzywuzzy import fuzz
import datetime
import json
import os

# Setup PRAW with your Reddit API credentials
reddit = praw.Reddit(client_id="XXXX",
                     client_secret="XXXX",
                     user_agent="SurfBot by u/Swimmer")

# List of top cryptocurrency subreddits
subreddits = ['Bitcoin', 'ethereum', 'CryptoCurrency','CryptoMarkets','Ethereum','btc','BitcoinMarkets']  # Add more subreddits

# Phrases for sentiment analysis
neutral_phrases = ["cryptocurrency", "bitcoin", "ethereum", "litecoin", "tether usd", "bnb", "binance coin", "btc", "ltc", "solana", "usdc", "robinhood crypto", "binance", "coinbase"]
positive_phrases = ["buy","buy crypto", "crypto summer", "crypto etf", "blockchain etf", "blockchain fund", "crypto fund", "institutional crypto", "institutional blockchain", "to the moon", "crypto bullrun", "buy crypto","bull","bull market","bullish",]
negative_phrases = ["sell","HODL","crypto fraud", "crypto regulations", "crypto etfs", "sell crypto", "crypto winter", "crypto burst", "crypto bubble", "sinking ship", "lost cause","sell","HODL","Pump and Dump","Rug Pull"]

# Function to normalize text
def normalize_text(text):
    text = text.lower()
    text = ' '.join(text.split())  # Remove extra spaces
    return text

# Function for fuzzy phrase matching
def fuzzy_phrase_count(text_data, phrase):
    return sum(fuzz.partial_ratio(normalize_text(text), normalize_text(phrase)) > 80 for text in text_data)

# Function to fetch post titles
def fetch_post_titles(subreddit_name, time_filter):
    subreddit = reddit.subreddit(subreddit_name)
    return [submission.title for submission in subreddit.top(time_filter=time_filter, limit=None)]

# Fetch post titles for different time periods
def fetch_data_for_all_subreddits(subreddits, time_filter):
    all_titles = []
    for subreddit_name in subreddits:
        titles = fetch_post_titles(subreddit_name, time_filter)
        all_titles.extend(titles)
    return all_titles

# Functions for caching data
def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return None

def should_update_data(filename, hours=8):
    if not os.path.exists(filename):
        return True
    file_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
    if (datetime.datetime.now() - file_mod_time) > datetime.timedelta(hours=hours):
        return True
    return False

# File names for cached data
file_3m = 'data_3m.json'
file_6m = 'data_6m.json'

# Update and load 3-month and 6-month data
if should_update_data(file_3m):
    data_3m = fetch_data_for_all_subreddits(subreddits, 'month')
    save_data_to_file(data_3m, file_3m)
else:
    data_3m = load_data_from_file(file_3m)

if should_update_data(file_6m):
    data_6m = fetch_data_for_all_subreddits(subreddits, 'year')
    save_data_to_file(data_6m, file_6m)
else:
    data_6m = load_data_from_file(file_6m)

# Always fetch 24-hour data
data_24h = fetch_data_for_all_subreddits(subreddits, 'day')

# Count classifications
positive_count, negative_count, neutral_count = 0, 0, 0
for title in data_24h:
    if any(fuzzy_phrase_count([title], phrase) for phrase in positive_phrases):
        positive_count += 1
    elif any(fuzzy_phrase_count([title], phrase) for phrase in negative_phrases):
        negative_count += 1
    else:
        neutral_count += 1

# Calculate weighted score components
volume_score_24h_6m = 35 * (volume_24h / max(1, volume_6m))
volume_score_24h_3m = 15 * (volume_24h / max(1, volume_3m))
positive_score = 40 * (positive_count / max(1, volume_24h))
negative_score = -40 * (negative_count / max(1, volume_24h))
neutral_score = 10 * (neutral_count / max(1, volume_24h))

print("positive score", positive_score)
print("neg score", negative_score)
print("neut score", neutral_score)

# Calculate final InvestorSentiment score
InvestorSentiment = volume_score_24h_6m + volume_score_24h_3m + positive_score + negative_score + neutral_score
InvestorSentiment = max(min(InvestorSentiment, 1000), -1000)

print("Investor Sentiment Score:", InvestorSentiment)


# In[ ]:


##Try Trade with the Sentiment


# In[ ]:


import requests
import time
import praw
import datetime
import json
import os
from fuzzywuzzy import fuzz
from sklearn.ensemble import RandomForestRegressor

# Reddit API credentials
reddit_client_id = 'vKj8rDxsVbevbSCp3Awndw'
reddit_client_secret = 'zt7SBd-_h3CfAXRYiCfKVR3Xc_MZKw'
reddit_user_agent = "SurfBot by u/Swimmer"

# Coinbase Pro API credentials
coinbase_api_key="XXXX"
coinbase_api_secret="XXXX"
coinbase_api_passphrase = 'YOUR_API_PASSPHRASE'

# Function to fetch spot price from Coinbase Pro
def fetch_price(currency_pair):
    url = f'https://api.pro.coinbase.com/products/{currency_pair}/ticker'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['price']
    else:
        raise Exception(f"Error fetching price for {currency_pair}")

# Placeholder function for fetching Bitcoin hash rate
def fetch_bitcoin_hash_rate():
    response = requests.get("https://blockchain.info/q/hashrate")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    return response

# Function to analyze investor sentiment from Reddit
def fetch_investor_sentiment():
    # Setup PRAW with your Reddit API credentials
    reddit = praw.Reddit(client_id="XXXX",
                         client_secret="XXXX",
                         user_agent="SurfBot by u/Swimmer")

    # List of top cryptocurrency subreddits
    subreddits = ['Bitcoin', 'ethereum', 'CryptoCurrency','CryptoMarkets','Ethereum','btc','BitcoinMarkets']  # Add more subreddits

    # Phrases for sentiment analysis
    neutral_phrases = ["cryptocurrency", "bitcoin", "ethereum", "litecoin", "tether usd", "bnb", "binance coin", "btc", "ltc", "solana", "usdc", "robinhood crypto", "binance", "coinbase"]
    positive_phrases = ["buy","buy crypto", "crypto summer", "crypto etf", "blockchain etf", "blockchain fund", "crypto fund", "institutional crypto", "institutional blockchain", "to the moon", "crypto bullrun", "buy crypto","bull","bull market","bullish",]
    negative_phrases = ["sell","HODL","crypto fraud", "crypto regulations", "crypto etfs", "sell crypto", "crypto winter", "crypto burst", "crypto bubble", "sinking ship", "lost cause","sell","HODL","Pump and Dump","Rug Pull"]

    # Function to normalize text
    def normalize_text(text):
        text = text.lower()
        text = ' '.join(text.split())  # Remove extra spaces
        return text

    # Function for fuzzy phrase matching
    def fuzzy_phrase_count(text_data, phrase):
        return sum(fuzz.partial_ratio(normalize_text(text), normalize_text(phrase)) > 80 for text in text_data)

    # Function to fetch post titles
    def fetch_post_titles(subreddit_name, time_filter):
        subreddit = reddit.subreddit(subreddit_name)
        return [submission.title for submission in subreddit.top(time_filter=time_filter, limit=None)]

    # Fetch post titles for different time periods
    def fetch_data_for_all_subreddits(subreddits, time_filter):
        all_titles = []
        for subreddit_name in subreddits:
            titles = fetch_post_titles(subreddit_name, time_filter)
            all_titles.extend(titles)
        return all_titles

    # Functions for caching data
    def save_data_to_file(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_data_from_file(filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return None

    def should_update_data(filename, hours=8):
        if not os.path.exists(filename):
            return True
        file_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
        if (datetime.datetime.now() - file_mod_time) > datetime.timedelta(hours=hours):
            return True
        return False

    # File names for cached data
    file_3m = 'data_3m.json'
    file_6m = 'data_6m.json'

    # Update and load 3-month and 6-month data
    if should_update_data(file_3m):
        data_3m = fetch_data_for_all_subreddits(subreddits, 'month')
        save_data_to_file(data_3m, file_3m)
    else:
        data_3m = load_data_from_file(file_3m)

    if should_update_data(file_6m):
        data_6m = fetch_data_for_all_subreddits(subreddits, 'year')
        save_data_to_file(data_6m, file_6m)
    else:
        data_6m = load_data_from_file(file_6m)

    # Always fetch 24-hour data
    data_24h = fetch_data_for_all_subreddits(subreddits, 'day')

    # Count classifications
    positive_count, negative_count, neutral_count = 0, 0, 0
    for title in data_24h:
        if any(fuzzy_phrase_count([title], phrase) for phrase in positive_phrases):
            positive_count += 1
        elif any(fuzzy_phrase_count([title], phrase) for phrase in negative_phrases):
            negative_count += 1
        else:
            neutral_count += 1

    # Calculate weighted score components
    volume_score_24h_6m = 35 * (volume_24h / max(1, volume_6m))
    volume_score_24h_3m = 15 * (volume_24h / max(1, volume_3m))
    positive_score = 40 * (positive_count / max(1, volume_24h))
    negative_score = -40 * (negative_count / max(1, volume_24h))
    neutral_score = 10 * (neutral_count / max(1, volume_24h))

    print("positive score", positive_score)
    print("neg score", negative_score)
    print("neut score", neutral_score)

    # Calculate final InvestorSentiment score
    InvestorSentiment = volume_score_24h_6m + volume_score_24h_3m + positive_score + negative_score + neutral_score
    InvestorSentiment = max(min(InvestorSentiment, 1000), -1000)

    print("Investor Sentiment Score:", InvestorSentiment)

    return InvestorSentiment

# Account class to manage transactions
class Account:
    def __init__(self, amountUSD, amountLTC, valueLTC, spentOnLTC, costBasisLTC):
        self.amountUSD = amountUSD
        self.amountLTC = amountLTC
        self.valueLTC = valueLTC
        self.spentOnLTC = spentOnLTC
        self.costBasisLTC = costBasisLTC

    def log_transaction(self, transaction_type, amountOrder, priceOrder):
        with open('account_log.txt', 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = (f"{timestamp}: {transaction_type} - Amount Order: {amountOrder}, Price Order: {priceOrder}, "
                         f"USD: {self.amountUSD}, LTC: {self.amountLTC}, Value LTC: {self.valueLTC}, "
                         f"Spent on LTC: {self.spentOnLTC}, Cost Basis LTC: {self.costBasisLTC}\n")
            file.write(log_entry)

    def buy_ltc(self, amountOrder, priceOrder):
        self.amountUSD -= priceOrder * amountOrder
        self.amountLTC += amountOrder
        self.valueLTC = self.amountLTC * priceOrder
        self.spentOnLTC += priceOrder * amountOrder
        self.update_cost_basis()
        self.log_transaction("BUY", amountOrder, priceOrder)

    def sell_ltc(self, amountOrder, priceOrder):
        self.amountUSD += priceOrder * amountOrder
        self.amountLTC -= amountOrder
        self.spentOnLTC -= priceOrder * amountOrder
        self.update_cost_basis()
        self.log_transaction("SELL", amountOrder, priceOrder)

    def update_cost_basis(self):
        if self.amountLTC != 0:
            self.costBasisLTC = self.spentOnLTC / self.amountLTC
        else:
            self.spentOnLTC = 0
            self.costBasisLTC = 0

    def get_Account(self, spotLTC):
        self.valueLTC = self.amountLTC * spotLTC
        self.update_cost_basis()
        print('Account Status', '- USD', self.amountUSD, '- LTC', self.amountLTC, 'LTC Value', self.valueLTC, 'Cost Basis', self.costBasisLTC)

# Function to execute trade (buy/sell)
def execute_trade(action, amount, currency_pair, account):
    print(f"{action} {amount} of {currency_pair}")
    if action == 'Buy':
        account.buy_ltc(amount, fetch_price(currency_pair))
        # Add actual trading logic here using Coinbase Pro API

    if action == 'Sell':
        account.sell_ltc(amount, fetch_price(currency_pair))
        # Add actual trading logic here using Coinbase Pro API

    print(f"{action} {amount} of {currency_pair}")
    # Add actual trading logic here using Coinbase Pro API

# Function to make trading decisions
def trade_logic(account):
    litecoin_price = fetch_price('LTC-USD')
    bitcoin_price = fetch_price('BTC-USD')
    bitcoin_hash_rate = fetch_bitcoin_hash_rate()
    investor_sentiment = fetch_investor_sentiment()

    if float(litecoin_price) > 60 and investor_sentiment > 250:
        execute_trade('Buy', 1, 'LTC-USD', account)  # Buying 1 Litecoin
    else:
        execute_trade('Sell', 1, 'LTC-USD', account)  # Selling 1 Litecoin


# Main function to run the bot
def run_bot():
    try:
        account = Account(1000, 0, 0, 0, 0)
        while True:
            trade_logic(account)
            print("Trade executed at", time.strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(60)
    except KeyboardInterrupt:
        print("Bot stopped manually")

# Start the bot
run_bot()


# In[ ]:





# In[ ]:


import requests
import time
import praw
import datetime
import json
import os
from fuzzywuzzy import fuzz
from sklearn.ensemble import RandomForestRegressor

# Reddit API credentials
reddit_client_id = 'vKj8rDxsVbevbSCp3Awndw'
reddit_client_secret = 'zt7SBd-_h3CfAXRYiCfKVR3Xc_MZKw'
reddit_user_agent = "SurfBot by u/Swimmer"

# Coinbase Pro API credentials
coinbase_api_key="XXXX"
coinbase_api_secret="XXXX"
coinbase_api_passphrase = 'YOUR_API_PASSPHRASE'

# Function to fetch spot price from Coinbase Pro
def fetch_price(currency_pair):
    url = f'https://api.pro.coinbase.com/products/{currency_pair}/ticker'
    response = requests.get(url)
    if response.status_code == 200:
        price = response.json()['price']
        return float(price)  # Convert price to float
    else:
        raise Exception(f"Error fetching price for {currency_pair}")

# Placeholder function for fetching Bitcoin hash rate
def fetch_bitcoin_hash_rate():
    response = requests.get("https://blockchain.info/q/hashrate")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    return response

# Function to analyze investor sentiment from Reddit
def fetch_investor_sentiment():
    # Setup PRAW with your Reddit API credentials
    reddit = praw.Reddit(client_id=reddit_client_id,
                         client_secret=reddit_client_secret,
                         user_agent=reddit_user_agent)

    # List of top cryptocurrency subreddits
    subreddits = ['Bitcoin', 'ethereum', 'CryptoCurrency','CryptoMarkets','Ethereum','btc','BitcoinMarkets']  # Add more subreddits

    # Phrases for sentiment analysis
    neutral_phrases = ["cryptocurrency", "bitcoin", "ethereum", "litecoin", "tether usd", "bnb", "binance coin", "btc", "ltc", "solana", "usdc", "robinhood crypto", "binance", "coinbase"]
    positive_phrases = ["buy","buy crypto", "crypto summer", "crypto etf", "blockchain etf", "blockchain fund", "crypto fund", "institutional crypto", "institutional blockchain", "to the moon", "crypto bullrun", "buy crypto","bull","bull market","bullish"]
    negative_phrases = ["sell","HODL","crypto fraud", "crypto regulations", "crypto etfs", "sell crypto", "crypto winter", "crypto burst", "crypto bubble", "sinking ship", "lost cause","sell","HODL","Pump and Dump","Rug Pull"]

    # Function to normalize text
    def normalize_text(text):
        text = text.lower()
        text = ' '.join(text.split())  # Remove extra spaces
        return text

    # Function for fuzzy phrase matching
    def fuzzy_phrase_count(text_data, phrase):
        return sum(fuzz.partial_ratio(normalize_text(text), normalize_text(phrase)) > 80 for text in text_data)

    # Function to fetch post titles
    def fetch_post_titles(subreddit_name, time_filter):
        subreddit = reddit.subreddit(subreddit_name)
        return [submission.title for submission in subreddit.top(time_filter=time_filter, limit=None)]

    # Fetch post titles for different time periods
    def fetch_data_for_all_subreddits(subreddits, time_filter):
        all_titles = []
        for subreddit_name in subreddits:
            titles = fetch_post_titles(subreddit_name, time_filter)
            all_titles.extend(titles)
        return all_titles

    # Functions for caching data
    def save_data_to_file(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_data_from_file(filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return None

    def should_update_data(filename, hours=8):
        if not os.path.exists(filename):
            return True
        file_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
        if (datetime.datetime.now() - file_mod_time) > datetime.timedelta(hours=hours):
            return True
        return False

    # File names for cached data
    file_3m = 'data_3m.json'
    file_6m = 'data_6m.json'

    # Update and load 3-month and 6-month data
    if should_update_data(file_3m):
        data_3m = fetch_data_for_all_subreddits(subreddits, 'month')
        save_data_to_file(data_3m, file_3m)
    else:
        data_3m = load_data_from_file(file_3m)

    if should_update_data(file_6m):
        data_6m = fetch_data_for_all_subreddits(subreddits, 'year')
        save_data_to_file(data_6m, file_6m)
    else:
        data_6m = load_data_from_file(file_6m)

    # Always fetch 24-hour data
    data_24h = fetch_data_for_all_subreddits(subreddits, 'day')

    # Count classifications
    positive_count, negative_count, neutral_count = 0, 0, 0
    for title in data_24h:
        if any(fuzzy_phrase_count([title], phrase) for phrase in positive_phrases):
            positive_count += 1
        elif any(fuzzy_phrase_count([title], phrase) for phrase in negative_phrases):
            negative_count += 1
        else:
            neutral_count += 1

    # Calculate weighted score components
    # Note: The following variables need to be defined or fetched: volume_24h, volume_6m, volume_3m
    volume_score_24h_6m = 35 * (volume_24h / max(1, volume_6m))
    volume_score_24h_3m = 15 * (volume_24h / max(1, volume_3m))
    positive_score = 40 * (positive_count / max(1, volume_24h))
    negative_score = -40 * (negative_count / max(1, volume_24h))
    neutral_score = 10 * (neutral_count / max(1, volume_24h))

    print("positive score", positive_score)
    print("neg score", negative_score)
    print("neut score", neutral_score)

    # Calculate final InvestorSentiment score
    InvestorSentiment = volume_score_24h_6m + volume_score_24h_3m + positive_score + negative_score + neutral_score
    InvestorSentiment = max(min(InvestorSentiment, 1000), -1000)

    print("Investor Sentiment Score:", InvestorSentiment)

    return InvestorSentiment

# Account class to manage transactions
class Account:
    def __init__(self, amountUSD, amountLTC, valueLTC, spentOnLTC, costBasisLTC):
        self.amountUSD = amountUSD
        self.amountLTC = amountLTC
        self.valueLTC = valueLTC
        self.spentOnLTC = spentOnLTC
        self.costBasisLTC = costBasisLTC

    def log_transaction(self, transaction_type, amountOrder, priceOrder):
        with open('account_log.txt', 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = (f"{timestamp}: {transaction_type} - Amount Order: {amountOrder}, Price Order: {priceOrder}, "
                         f"USD: {self.amountUSD}, LTC: {self.amountLTC}, Value LTC: {self.valueLTC}, "
                         f"Spent on LTC: {self.spentOnLTC}, Cost Basis LTC: {self.costBasisLTC}\n")
            file.write(log_entry)

    def buy_ltc(self, amountOrder, priceOrder):
        amountOrder = float(amountOrder)
        priceOrder = float(priceOrder)
        self.amountUSD -= priceOrder * amountOrder
        self.amountLTC += amountOrder
        self.valueLTC = self.amountLTC * priceOrder
        self.spentOnLTC += priceOrder * amountOrder
        self.update_cost_basis()
        self.log_transaction("BUY", amountOrder, priceOrder)

    def sell_ltc(self, amountOrder, priceOrder):
        amountOrder = float(amountOrder)
        priceOrder = float(priceOrder)
        self.amountUSD += priceOrder * amountOrder
        self.amountLTC -= amountOrder
        self.spentOnLTC -= priceOrder * amountOrder
        self.update_cost_basis()
        self.log_transaction("SELL", amountOrder, priceOrder)

    def update_cost_basis(self):
        if self.amountLTC != 0:
            self.costBasisLTC = self.spentOnLTC / self.amountLTC
        else:
            self.spentOnLTC = 0
            self.costBasisLTC = 0

    def get_Account(self, spotLTC):
        self.valueLTC = self.amountLTC * spotLTC
        self.update_cost_basis()
        print('Account Status', '- USD', self.amountUSD, '- LTC', self.amountLTC, 'LTC Value', self.valueLTC, 'Cost Basis', self.costBasisLTC)

# Function to execute trade (buy/sell)
def execute_trade(action, amount, currency_pair, account):
    print(f"{action} {amount} of {currency_pair}")
    if action == 'Buy':
        account.buy_ltc(amount, fetch_price(currency_pair))
        # Add actual trading logic here using Coinbase Pro API

    if action == 'Sell':
        account.sell_ltc(amount, fetch_price(currency_pair))
        # Add actual trading logic here using Coinbase Pro API

    print(f"{action} {amount} of {currency_pair}")
    # Add actual trading logic here using Coinbase Pro API

# Function to make trading decisions
def trade_logic(account):
    litecoin_price = fetch_price('LTC-USD')
    bitcoin_price = fetch_price('BTC-USD')
    bitcoin_hash_rate = fetch_bitcoin_hash_rate()
    investor_sentiment = fetch_investor_sentiment()

    if float(litecoin_price) > 60 and investor_sentiment > 250:
        execute_trade('Buy', 1, 'LTC-USD', account)  # Buying 1 Litecoin
    else:
        execute_trade('Sell', 1, 'LTC-USD', account)  # Selling 1 Litecoin

# Main function to run the bot
def run_bot():
    try:
        account = Account(1000, 0, 0, 0, 0)
        while True:
            trade_logic(account)
            print("Trade executed at", time.strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(5)
    except KeyboardInterrupt:
        print("Bot stopped manually")

# Start the bot
run_bot()


# In[ ]:





# In[90]:


import requests
import time
import praw
import datetime
import json
import os
from fuzzywuzzy import fuzz
from sklearn.ensemble import RandomForestRegressor

# Reddit API credentials
reddit_client_id = 'vKj8rDxsVbevbSCp3Awndw'
reddit_client_secret = 'zt7SBd-_h3CfAXRYiCfKVR3Xc_MZKw'
reddit_user_agent = "SurfBot by u/Swimmer"

# Coinbase Pro API credentials
coinbase_api_key="XXXX"
coinbase_api_secret="XXXX"
coinbase_api_passphrase = 'YOUR_API_PASSPHRASE'

# Function to fetch spot price from Coinbase Pro
def fetch_price(currency_pair):
    url = f'https://api.pro.coinbase.com/products/{currency_pair}/ticker'
    response = requests.get(url)
    if response.status_code == 200:
        price = response.json()['price']
        return float(price)  # Convert price to float
    else:
        raise Exception(f"Error fetching price for {currency_pair}")

# Placeholder function for fetching Bitcoin hash rate
def fetch_bitcoin_hash_rate():
    response = requests.get("https://blockchain.info/q/hashrate")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    return response

# Function to analyze investor sentiment from Reddit
def fetch_investor_sentiment():
    # Setup PRAW with your Reddit API credentials
    reddit = praw.Reddit(client_id=reddit_client_id,
                         client_secret=reddit_client_secret,
                         user_agent=reddit_user_agent)

    # List of top cryptocurrency subreddits
    subreddits = ['Bitcoin', 'ethereum', 'CryptoCurrency','CryptoMarkets','Ethereum','btc','BitcoinMarkets']  # Add more subreddits

    # Phrases for sentiment analysis
    neutral_phrases = ["cryptocurrency", "bitcoin", "ethereum", "litecoin", "tether usd", "bnb", "binance coin", "btc", "ltc", "solana", "usdc", "robinhood crypto", "binance", "coinbase"]
    positive_phrases = ["buy","buy crypto", "crypto summer", "crypto etf", "blockchain etf", "blockchain fund", "crypto fund", "institutional crypto", "institutional blockchain", "to the moon", "crypto bullrun", "buy crypto","bull","bull market","bullish"]
    negative_phrases = ["sell","HODL","crypto fraud", "crypto regulations", "crypto etfs", "sell crypto", "crypto winter", "crypto burst", "crypto bubble", "sinking ship", "lost cause","sell","HODL","Pump and Dump","Rug Pull"]

    # Function to normalize text
    def normalize_text(text):
        text = text.lower()
        text = ' '.join(text.split())  # Remove extra spaces
        return text

    # Function for fuzzy phrase matching
    def fuzzy_phrase_count(text_data, phrase):
        return sum(fuzz.partial_ratio(normalize_text(text), normalize_text(phrase)) > 80 for text in text_data)

    # Function to fetch post titles
    def fetch_post_titles(subreddit_name, time_filter):
        subreddit = reddit.subreddit(subreddit_name)
        return [submission.title for submission in subreddit.top(time_filter=time_filter, limit=None)]

    # Fetch post titles for different time periods
    def fetch_data_for_all_subreddits(subreddits, time_filter):
        all_titles = []
        for subreddit_name in subreddits:
            titles = fetch_post_titles(subreddit_name, time_filter)
            all_titles.extend(titles)
        return all_titles

    # Functions for caching data
    def save_data_to_file(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_data_from_file(filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return None

    def should_update_data(filename, hours=8):
        if not os.path.exists(filename):
            return True
        file_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
        if (datetime.datetime.now() - file_mod_time) > datetime.timedelta(hours=hours):
            return True
        return False

    # File names for cached data
    file_3m = 'data_3m.json'
    file_6m = 'data_6m.json'

    # Update and load 3-month and 6-month data
    if should_update_data(file_3m):
        data_3m = fetch_data_for_all_subreddits(subreddits, 'month')
        save_data_to_file(data_3m, file_3m)
    else:
        data_3m = load_data_from_file(file_3m)

    if should_update_data(file_6m):
        data_6m = fetch_data_for_all_subreddits(subreddits, 'year')
        save_data_to_file(data_6m, file_6m)
    else:
        data_6m = load_data_from_file(file_6m)

    # Always fetch 24-hour data
    data_24h = fetch_data_for_all_subreddits(subreddits, 'day')

    # Count classifications
    positive_count, negative_count, neutral_count = 0, 0, 0
    for title in data_24h:
        if any(fuzzy_phrase_count([title], phrase) for phrase in positive_phrases):
            positive_count += 1
        elif any(fuzzy_phrase_count([title], phrase) for phrase in negative_phrases):
            negative_count += 1
        else:
            neutral_count += 1

    # Calculate weighted score components
    # Note: The following variables need to be defined or fetched: volume_24h, volume_6m, volume_3m
    volume_score_24h_6m = 35 * (volume_24h / max(1, volume_6m))
    volume_score_24h_3m = 15 * (volume_24h / max(1, volume_3m))
    positive_score = 40 * (positive_count / max(1, volume_24h))
    negative_score = -40 * (negative_count / max(1, volume_24h))
    neutral_score = 10 * (neutral_count / max(1, volume_24h))

    print("positive score", positive_score)
    print("neg score", negative_score)
    print("neut score", neutral_score)

    # Calculate final InvestorSentiment score
    InvestorSentiment = volume_score_24h_6m + volume_score_24h_3m + positive_score + negative_score + neutral_score
    InvestorSentiment = max(min(InvestorSentiment, 1000), -1000)

    print("Investor Sentiment Score:", InvestorSentiment)

    return InvestorSentiment

# Account class to manage transactions: DELETE WHEN INCOPORATING REAL TRADING
class Account:
    def __init__(self, amountUSD, amountLTC, valueLTC, spentOnLTC, costBasisLTC):
        self.amountUSD = amountUSD
        self.amountLTC = amountLTC
        self.valueLTC = valueLTC
        self.spentOnLTC = spentOnLTC
        self.costBasisLTC = costBasisLTC

    def log_transaction(self, transaction_type, amountOrder, priceOrder):
        with open('account_log.txt', 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = (f"{timestamp}: {transaction_type} - Amount Order: {amountOrder}, Price Order: {priceOrder}, "
                         f"USD: {self.amountUSD}, LTC: {self.amountLTC}, Value LTC: {self.valueLTC}, "
                         f"Spent on LTC: {self.spentOnLTC}, Cost Basis LTC: {self.costBasisLTC}\n")
            file.write(log_entry)

    def buy_ltc(self, amountOrder, priceOrder):
        amountOrder = float(amountOrder)
        priceOrder = float(priceOrder)
        self.amountUSD -= priceOrder * amountOrder
        self.amountLTC += amountOrder
        self.valueLTC = self.amountLTC * priceOrder
        self.spentOnLTC += priceOrder * amountOrder
        self.update_cost_basis()
        self.log_transaction("BUY", amountOrder, priceOrder)

    def sell_ltc(self, amountOrder, priceOrder):
        amountOrder = float(amountOrder)
        priceOrder = float(priceOrder)
        self.amountUSD += priceOrder * amountOrder
        self.amountLTC -= amountOrder
        self.spentOnLTC -= priceOrder * amountOrder
        self.update_cost_basis()
        self.log_transaction("SELL", amountOrder, priceOrder)

    def update_cost_basis(self):
        if self.amountLTC != 0:
            self.costBasisLTC = self.spentOnLTC / self.amountLTC
        else:
            self.spentOnLTC = 0
            self.costBasisLTC = 0

    def get_Account(self, spotLTC):
        self.valueLTC = self.amountLTC * spotLTC
        self.update_cost_basis()
        print('Account Status', '- USD', self.amountUSD, '- LTC', self.amountLTC, 'LTC Value', self.valueLTC, 'Cost Basis', self.costBasisLTC)

# Establish Account

account = Account(1000, 0, 0, 0, 0)

# Function to execute trade (buy/sell)
def execute_trade(action, amount, currency_pair, account):
    print(f"{action} {amount} of {currency_pair}")
    if action == 'Buy':
        account.buy_ltc(amount, fetch_price(currency_pair))
        # Add actual trading logic here using Coinbase Pro API

    if action == 'Sell':
        account.sell_ltc(amount, fetch_price(currency_pair))
        # Add actual trading logic here using Coinbase Pro API

    print(f"{action} {amount} of {currency_pair}")
    # Add actual trading logic here using Coinbase Pro API

# Function to make trading decisions
def trade_logic(account):
    litecoin_price = fetch_price('LTC-USD')
    bitcoin_price = fetch_price('BTC-USD')
    bitcoin_hash_rate = fetch_bitcoin_hash_rate()
    investor_sentiment = fetch_investor_sentiment()

    if float(litecoin_price) > 70.63 and investor_sentiment > 150:
        execute_trade('Buy', 1, 'LTC-USD', account)  # Buying 1 Litecoin
    else:
        execute_trade('Sell', 1, 'LTC-USD', account)  # Selling 1 Litecoin

# Main function to run the bot
def run_bot():
    try:
        print(1)
        while True:
            trade_logic(account)
            print("Trade executed at", time.strftime("%Y-%m-%d %H:%M:%S"))
            #time.sleep(1)
            print(2)
    except KeyboardInterrupt:
        print("Bot stopped manually")

# Start the bot
run_bot()


# In[ ]:





