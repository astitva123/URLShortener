
url_store = {}

def store(original_url, short_url):
    url_store[short_url] = original_url

def retrieve(short_url):
    if short_url in url_store:
        return url_store[short_url]
    else:
        return ""