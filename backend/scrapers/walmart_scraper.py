import requests
from bs4 import BeautifulSoup

class WalmartScraper:
    def __init__(self, product_name):
        self.product_name = product_name
        self.base_url = 'https://www.walmart.com/search/?query=' + product_name.replace(' ', '%20')

    def get_product_data(self):
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        
        for item in soup.find_all('div', {'class': 'search-result-product'}):
            title = item.find('a', {'class': 'product-title-link'}).text.strip()
            price = item.find('span', {'class': 'price'}).text.strip() if item.find('span', {'class': 'price'}) else 'N/A'
            link = 'https://www.walmart.com' + item.find('a', {'class': 'product-title-link'})['href']
            products.append({'title': title, 'price': price, 'link': link})
        
        return products

# Example usage
if __name__ == '__main__':
    product_name = 'laptop'  # example product
    scraper = WalmartScraper(product_name)
    product_data = scraper.get_product_data()
    for product in product_data:
        print(product)