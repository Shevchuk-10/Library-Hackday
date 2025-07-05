import dns.resolver

def get_dns_records(domain):
    records = {}
    for record_type in ["A", "MX", "NS", "TXT"]:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [r.to_text() for r in answers]
        except Exception:
            records[record_type] = []
    return records
