#!/usr/bin/env python3
"""
Module for caching web pages with expiration and access count tracking.
"""

import redis
import requests
from typing import Callable

# Initialize Redis client
redis_client = redis.Redis()


def count_url_access(func: Callable) -> Callable:
    """
    Decorator to count the number of times a URL has been accessed.
    """
    def wrapper(url: str) -> str:
        # Increment the access count for this URL
        redis_client.incr(f"count:{url}")
        return func(url)

    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """
    Fetches the content of a URL,
    caching it with an expiration time of 10 seconds.
    """
    cached_content = redis_client.get(url)

    # Return cached content if available
    if cached_content:
        return cached_content.decode("utf-8")

    # Fetch the content if not in cache
    response = requests.get(url)
    content = response.text

    # Cache the content with a 10-second expiration
    redis_client.setex(url, 10, content)

    return content
