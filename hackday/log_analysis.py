def search_logs_for_ip(log_path, ip_address):
    try:
        with open(log_path) as f:
            return [line for line in f if ip_address in line]
    except FileNotFoundError:
        return []
