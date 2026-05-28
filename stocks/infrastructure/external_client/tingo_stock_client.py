"""Functions for fetching stock and crypto data from the Tiingo API."""

import requests
from django.conf import settings

API_KEY = settings.API_KEY

headers = {"Content-Type": "application/json", "Authorization": f"Token {API_KEY}"}


def get_search_data(stock_name: str) -> list:
    """Search for a stock by name via the Tiingo API."""
    url = f"https://api.tiingo.com/tiingo/utilities/search?query={stock_name}"
    response = requests.get(url, headers=headers, timeout=10)
    return response.json()


def get_price_information(stock_code: str) -> list:
    """Get daily price data for a stock."""
    url = f"https://api.tiingo.com/tiingo/daily/{stock_code}/prices"
    response = requests.get(url, headers=headers, timeout=10)
    return response.json()


def get_meta_data(stock_code: str) -> dict:
    """Get metadata for a stock."""
    url = f"https://api.tiingo.com/tiingo/daily/{stock_code}"
    response = requests.get(url, headers=headers, timeout=10)
    return response.json()


def list_of_crypto_data() -> list:
    """List all available crypto currencies from Tiingo."""
    url = "https://api.tiingo.com/tiingo/crypto"
    response = requests.get(url, headers=headers, timeout=10)
    return response.json()


def get_stocks_fundementals() -> list:
    """Get fundamentals definitions from Tiingo."""
    url = "https://api.tiingo.com/tiingo/fundamentals/definitions"
    response = requests.get(url, headers=headers, timeout=10)
    return response.json()
