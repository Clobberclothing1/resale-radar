
from ebaysdk.finding import Connection as Finding
import statistics

def ebay_price_stats(query: str):
    api = Finding(appid="YOUR_EBAY_APP_ID", config_file=None)
    response = api.execute('findCompletedItems', {
        'keywords': query,
        'itemFilter': [{'name': 'SoldItemsOnly', 'value': True}],
        'paginationInput': {'entriesPerPage': 50}
    })

    items = response.reply.searchResult.item
    prices = [float(it.sellingStatus.currentPrice.value) for it in items] if items else [0]
    return {
        "low": min(prices),
        "median": statistics.median(prices),
        "high": max(prices)
    }
