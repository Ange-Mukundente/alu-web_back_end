#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()

def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data and tracks request count.'''
    @wraps(method)
    def invoker(url: str) -> str:
        '''The wrapper function for caching the output.'''
        # Increment the request count
        redis_store.incr(f'count:{url}')
        
        # Check if result is already cached
        cached_result = redis_store.get(f'result:{url}')
        if cached_result:
            return cached_result.decode('utf-8')
        
        # Fetch data from URL and cache it
        result = method(url)
        redis_store.setex(f'result:{url}', 10, result)  # Cache expires after 10 seconds
        
        return result
    return invoker

@data_cacher
def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response.'''
    return requests.get(url).text
