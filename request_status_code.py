"""
In each second i, a gateway receives a request from the domain request[i].
The gateway allows at most 2 successful requests from a domain within 5 seconds,
and at most 5 successful requests within 30 seconds.
Given the array requests, for each request
return the string
"(status: 200, message: OK)" if the request can be processed.
Otherwise, return "(status: 429, message: Too many requests)".

Example:
Suppose n = 9 and requests = [
"www.xyz.com",
"www.abc.com",
"www.xyz.com",
"www.pqr.com",
"www.abc.com",
"www.xyz.com",
"www.xyz.com",
"www.abc.com",
"www.xyz.com"
]
"""

from collections import defaultdict, deque


def process_requests(requests):
    domain_counts_5s = defaultdict(deque)
    domain_counts_30s = defaultdict(deque)
    results = []

    for i, requests in enumerate(requests):
        while domain_counts_5s[requests] and domain_counts_5s[requests][0] <= i - 5:
            domain_counts_5s[requests].popleft()
        if len(domain_counts_5s[requests]) >= 2:
            results.append("(status: 429, message: Too many requests)")
            continue

        while domain_counts_30s[requests] and domain_counts_30s[requests][0] <= i - 30:
            domain_counts_30s[requests].popleft()
        if len(domain_counts_30s[requests]) >= 5:
            results.append("(status: 429, message: Too many requests)")
            continue

        domain_counts_5s[requests].append(i)
        domain_counts_30s[requests].append(i)
        results.append("(status: 200, message: OK)")
    return results


# Test the function
requests = [
    "www.xyz.com",
    "www.abc.com",
    "www.xyz.com",
    "www.pqr.com",
    "www.abc.com",
    "www.xyz.com",
    "www.xyz.com",
    "www.abc.com",
    "www.xyz.com"
]
print(process_requests(requests))
