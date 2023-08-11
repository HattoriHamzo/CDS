# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoffeeCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    coffee_name: str = scrapy.Field()
    coffee_price: str = scrapy.Field()
    coffee_image: str = scrapy.Field()
