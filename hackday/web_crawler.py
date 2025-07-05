import requests
from bs4 import BeautifulSoup

def crawl(url, depth=1):
    try:
        visited = set()
        def crawl_rec(u, d):
            if d == 0 or u in visited:
                return []
            visited.add(u)
            try:
                resp = requests.get(u)
                soup = BeautifulSoup(resp.text, 'html.parser')
                links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("http")]
                result = [(u, links)]
                for link in links:
                    result += crawl_rec(link, d-1)
                return result
            except:
                return []
        return crawl_rec(url, depth)
    except:
        return []
