from bs4 import BeautifulSoup

def extract_links(html):
    soup = BeautifulSoup(html, "html.parser")
    return [a['href'] for a in soup.find_all('a', href=True)]
