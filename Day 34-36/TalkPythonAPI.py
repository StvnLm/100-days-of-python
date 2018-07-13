import requests
import collections
from typing import List

ResultsNT = collections.namedtuple('Results', 'category, id, url, title, description')

def get_search_result(searchTerm: str) -> List[ResultsNT]:
    url = f'http://search.talkpython.fm/api/search?q={searchTerm}'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()

    results = []
    for r in response.get('results'):
        results.append(ResultsNT(**r))
    return results
