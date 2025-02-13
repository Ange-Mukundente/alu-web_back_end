#!/usr/bin/env python3
"""
Module for implementing a web page caching system
"""
import redis
import requests
from functools import wraps
from typing import Callable
from datetime import timedelta


def cache_decorator(fn: Callable) -> Callable:
    """Decorator to cache the result of get_page function"""
    @wraps(fn)
    def wrapper(url: str) -> str:
        """Wrapper function"""
        redis_client = redis.Redis()
        
        # Create keys for cache and count
        cache_key = f"cache:{url}"
        count_key = f"count:{url}"
        
        # Get cached page if it exists
        cached_page = redis_client.get(cache_key)
        if cached_page:
            # Increment access count
            redis_client.incr(count_key)
            return cached_page.decode('utf-8')
        
        # If not cached, get the page content
        page_content = fn(url)
        
        # Cache the content with 10 seconds expiration
        redis_client.setex(cache_key, timedelta(seconds=10), page_content)
        
        # Initialize or increment the access count
        redis_client.incr(count_key)
        
        return page_content
    
    return wrapper


@cache_decorator
def get_page(url: str) -> str:
    """
    Get the HTML content of a URL
    
    Args:
        url: URL to fetch
        
    Returns:
        HTML content of the URL
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    # Example usage:
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.example.com"
    page_content = get_page(url)
    print(page_content)
