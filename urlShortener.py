from hashlib import sha256

def shortenUrl(url):
    short_url = sha256(url.encode()).hexdigest()[:6]
    return short_url