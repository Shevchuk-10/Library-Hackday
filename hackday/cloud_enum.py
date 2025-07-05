import socket

def is_bucket_open(bucket_name):
    try:
        ip = socket.gethostbyname(f"{bucket_name}.s3.amazonaws.com")
        return True
    except socket.gaierror:
        return False
