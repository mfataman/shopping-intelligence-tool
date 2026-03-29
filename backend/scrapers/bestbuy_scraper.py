import requests
from bs4 import BeautifulSoup

class BestBuyScraper:
    def __init__(self, product_name):
        self.product_name = product_name
        self.base_url = 'https://www.bestbuy.com/'

    def search_product(self):
        search_url = f'{self.base_url}site/searchpage.jsp?st={self.product_name}'
        response = requests.get(search_url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def parse_results(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        product_list = []
        for item in soup.find_all('div', class_='sku-item'):  # Adjust class as needed
            title = item.find('h4', class_='sku-header').text.strip() if item.find('h4', class_='sku-header') else 'N/A'
            price = item.find('div', class_='priceView-hero-price').text.strip() if item.find('div', class_='priceView-hero-price') else 'N/A'
            product_list.append({'title': title, 'price': price})
        return product_list

    def run(self):
        html_content = self.search_product()
        if html_content:
            products = self.parse_results(html_content)
            return products
        else:
            return []
