def search_username(username):
    platforms = ["github.com", "twitter.com", "instagram.com"]
    return [f"https://{site}/{username}" for site in platforms]
