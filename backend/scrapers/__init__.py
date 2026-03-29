# scraper module initialization

from .scraper1 import Scraper1
from .scraper2 import Scraper2

class ScraperFactory:
    @staticmethod
    def create_scraper(scraper_type):
        if scraper_type == 'scraper1':
            return Scraper1()
        elif scraper_type == 'scraper2':
            return Scraper2()
        else:
            raise ValueError(f"Unknown scraper type: {scraper_type}")