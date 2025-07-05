import requests

def is_tor_exit_node(ip):
    try:
        url = f"https://check.torproject.org/torbulkexitlist"
        resp = requests.get(url)
        return ip in resp.text
    except Exception:
        return False
