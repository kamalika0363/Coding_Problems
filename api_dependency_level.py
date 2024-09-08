from typing import List
import re

def getResourceList(requests: List[str]) -> List[str]:
    def parse_resource(url):
        match = re.search(r'/resource(\d+)(/resource(\d+)(/resource(\d+))?)?', url)
        if match:
            return [group for group in match.groups()[::2] if group]
        return []

    def get_dependency_level(resource):
        return len(resource)

    resources = []
    for request in requests:
        parsed = parse_resource(request)
        if parsed:
            resources.append('/'.join(f"resource{id}" for id in parsed))

    # Sort resources by dependency level and then lexicographically
    return sorted(set(resources), key=lambda x: (get_dependency_level(x.split('/')), x))

# Test the function
requests = [
    "https://api.example.com/resource2/id/resource3/id2",
    "https://api.example.com/resource3/id/resource4/id6",
    "https://api.example.com/resource2/id",
    "https://api.example.com/resource1/id/resource3/id2"
]

result = getResourceList(requests)
print(result)