import psutil

def get_network_connections():
    return [conn._asdict() for conn in psutil.net_connections()]
