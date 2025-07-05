import requests

def check_proxy(proxy_url):
    try:
        r = requests.get("http://httpbin.org/ip", proxies={"http": proxy_url, "https": proxy_url}, timeout=5)
        return r.json()
    except:
        return None
