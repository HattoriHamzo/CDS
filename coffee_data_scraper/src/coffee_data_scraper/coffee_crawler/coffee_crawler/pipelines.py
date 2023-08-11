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
    """ """

    def process_item(
        self, item: CoffeeCrawlerItem, spider: Spider
    ) -> CoffeeCrawlerItem:
        """ """
        adapter: ItemAdapter = ItemAdapter(item)
        if adapter.get("coffee_price"):
            adapter["coffee_price"] = adapter["coffee_price"].replace(",", ".")

        return item


class JsonWriterPipeline:
    """ """

    def open_spider(self, spider: Spider) -> None:
        """ """
        self.file: TextIOWrapper = open(f"items.json", "w")
        self.file.write("[")
        self.first_item_written: bool = False

    def close_spider(self, spider: Spider) -> None:
        """ """
        self.file.write("\n]")
        self.file.close()

    def process_item(
        self, item: CoffeeCrawlerItem, spider: Spider
    ) -> CoffeeCrawlerItem:
        """ """
        if self.first_item_written:
            self.file.write(",\n")
        else:
            self.first_item_written: bool = True

        line: str = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False, indent=2)
        self.file.write(line)
        return item
