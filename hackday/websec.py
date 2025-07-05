import requests

def check_security_headers(url):
    try:
        r = requests.get(url)
        return {
            "Content-Security-Policy": r.headers.get("Content-Security-Policy"),
            "Strict-Transport-Security": r.headers.get("Strict-Transport-Security"),
            "X-Frame-Options": r.headers.get("X-Frame-Options")
        }
    except:
        return {}
