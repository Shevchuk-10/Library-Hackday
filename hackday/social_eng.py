import random

def generate_fake_login_page(domain="example.com"):
    return f"https://{domain}/login?session={random.randint(1000, 9999)}"
