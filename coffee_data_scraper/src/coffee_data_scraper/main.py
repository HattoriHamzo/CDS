from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from coffee_data_scraper.coffee_crawler.coffee_crawler.spiders.coffe_spider import (
    CoffeeSpider,
)


def main():
    """
    Main function to start the scraping process.
    """

    settings: dict = get_project_settings()

    process: CrawlerProcess = CrawlerProcess(settings)

    process.crawl(CoffeeSpider)

    process.start()


if __name__ == "__main__":
    main()
