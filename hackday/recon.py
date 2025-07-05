
import socket

def get_ip(hostname: str):
    try:
        return socket.gethostbyname(hostname)
    except Exception:
        return None
