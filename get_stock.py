from urllib.request import urlopen
from constants import CANYON_URL, HTML_SEARCH_TAG, HTML_TAG_LEN, SIZE_STOCK_LEN

def get_html(url):
    print(url)
    page = urlopen(url)
    
    html_bytes = page.read()
    return html_bytes.decode("utf-8")


def find_stock(html):
    sizes = []
    for i in range(4):
        index = html.find(HTML_SEARCH_TAG)
        sizes.append(html[index+HTML_TAG_LEN:index+HTML_TAG_LEN+SIZE_STOCK_LEN].strip())
        html = html[index+HTML_TAG_LEN+SIZE_STOCK_LEN:]
    return sizes

print(find_stock(get_html(CANYON_URL)))