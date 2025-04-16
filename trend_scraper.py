
import requests, bs4, pandas as pd

def vinted_trending():
    url = "https://www.vinted.co.uk/vinted-trending"
    html = bs4.BeautifulSoup(requests.get(url, timeout=10).text, "html.parser")
    tags = [t.text.strip() for t in html.select("a.TrendsItem")]
    return pd.Series(tags, name="Trending Brands")
