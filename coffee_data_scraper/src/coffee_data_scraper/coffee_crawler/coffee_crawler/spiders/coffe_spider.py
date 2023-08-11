import json
from typing import List
from coffee_data_scraper.coffee_crawler.coffee_crawler.items import CoffeeCrawlerItem
from coffee_data_scraper.utils.coffee_builder import build_base_coffee_types

from scrapy import Spider, Request
from coffee_data_scraper.infrastructure.config.settings import settings


class CoffeeSpider(Spider):
    """
    A Scrapy spider for crawling coffee-related information.

    Attributes:
        name (str): The name of the spider.
        _SCRAPY_REQUESTS_URL (List[str]): List of URLs to be used for scraping.
        custom_settings (dict): Custom settings for the spider, including pipelines.

    Note:
        The `_SCRAPY_REQUESTS_URL` attribute is loaded from settings.SCRAPY_REQUESTS_URL.
    """

    name: str = "coffe_spider"
    _SCRAPY_REQUESTS_URL: List[str] = json.loads(settings.SCRAPY_REQUESTS_URL)

    custom_settings: dict = {
        "ITEM_PIPELINES": {
            "coffee_data_scraper.coffee_crawler.coffee_crawler.pipelines.CoffeeCrawlerPipeline": 300,
            "coffee_data_scraper.coffee_crawler.coffee_crawler.pipelines.JsonWriterPipeline": 400,
        }
    }

    def start_requests(self) -> List[Request]:
        """
        Generate initial requests for scraping.

        Returns:
            List[Request]: A list of initial requests to start the scraping process.
        """
        urls: List[str] = self._SCRAPY_REQUESTS_URL

        requests: List[Request] = []

        for url in urls:
            request: Request = Request(url=url, callback=self.parse)
            requests.append(request)

        return requests

    def parse(self, response: str) -> CoffeeCrawlerItem:
        """
        Parses the response and extracts coffee information.

        Args:
            response (str): The response from the URL request.

        Yields:
            CoffeeCrawlerItem: An item containing coffee information.
        """

        coffee_types: List[str] = response.css(
            'div[data-widget_type="woocommerce-products.default"]'
        ).css('[class="nv-card-content-wrapper"]')

        yield from build_base_coffee_types(coffee_types=coffee_types)
