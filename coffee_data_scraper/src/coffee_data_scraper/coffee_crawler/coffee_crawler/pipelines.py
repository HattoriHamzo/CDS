# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from io import TextIOWrapper
import json
from coffee_data_scraper.coffee_crawler.coffee_crawler.items import CoffeeCrawlerItem
from itemadapter import ItemAdapter
from scrapy import Spider


class CoffeeCrawlerPipeline:
    """
    This class defines a pipeline for processing items scraped by the CoffeeCrawler spider.
    """

    def process_item(
        self, item: CoffeeCrawlerItem, spider: Spider
    ) -> CoffeeCrawlerItem:
        """
        Process the scraped item and perform necessary transformations.

        Args:
            item (CoffeeCrawlerItem): The scraped item to be processed.
            spider (Spider): The spider that scraped the item.

        Returns:
            CoffeeCrawlerItem: The processed item after transformations.
        """
        adapter: ItemAdapter = ItemAdapter(item)
        if adapter.get("coffee_price"):
            adapter["coffee_price"] = adapter["coffee_price"].replace(",", ".")

        return item


class JsonWriterPipeline:
    """
    This class defines a pipeline for writing scraped items to a JSON file.
    """

    def open_spider(self, spider: Spider) -> None:
        """
        Open the JSON file for writing and initialize necessary variables.

        Args:
            spider (Spider): The spider that was opened.
        """
        self.file: TextIOWrapper = open(f"items.json", "w")
        self.file.write("[")
        self.first_item_written: bool = False

    def close_spider(self, spider: Spider) -> None:
        """
        Close the JSON file after writing all items and finalize the structure.

        Args:
            spider (Spider): The spider that was closed.
        """
        self.file.write("\n]")
        self.file.close()

    def process_item(
        self, item: CoffeeCrawlerItem, spider: Spider
    ) -> CoffeeCrawlerItem:
        """
        Process and write the scraped item to the JSON file.

        Args:
            item (CoffeeCrawlerItem): The scraped item to be processed and written.
            spider (Spider): The spider that scraped the item.

        Returns:
            CoffeeCrawlerItem: The processed item to be passed to the next pipeline stage.
        """
        if self.first_item_written:
            self.file.write(",\n")
        else:
            self.first_item_written: bool = True

        line: str = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False, indent=2)
        self.file.write(line)
        return item
