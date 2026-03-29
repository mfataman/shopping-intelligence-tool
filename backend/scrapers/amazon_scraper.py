import requests
from bs4 import BeautifulSoup

class AmazonScraper:
    def __init__(self):
        self.base_url = 'https://www.amazon.com/s'  # Amazon search URL

    def search(self, query):
        # Perform a search on Amazon
        params = {'k': query}
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text

    def extract_prices(self, html_content):
        # Extract product prices from the search results
        soup = BeautifulSoup(html_content, 'html.parser')
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        prices = []
        for product in products:
            price = product.find('span', 'a-price')
            if price:
                price_amount = price.find('span', 'a-offscreen')
                if price_amount:
                    prices.append(price_amount.get_text())
        return prices

# Example usage:
# if __name__ == '__main__':
#     scraper = AmazonScraper()
#     html_content = scraper.search('laptop')
#     prices = scraper.extract_prices(html_content)
#     print(prices)
