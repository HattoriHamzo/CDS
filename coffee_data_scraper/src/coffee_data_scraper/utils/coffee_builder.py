from ast import List
from coffee_data_scraper.coffee_crawler.coffee_crawler.items import CoffeeCrawlerItem


def build_base_coffee_types(coffee_types: List[str]) -> CoffeeCrawlerItem:
    """
    Builds a list of CoffeeCrawlerItem instances based on the provided list of coffee types.

    Args:
        coffee_types (List[str]): A list of HTML elements representing coffee types.

    Yields:
        CoffeeCrawlerItem: A CoffeeCrawlerItem instance containing information about a coffee type.
    """
    for coffee in coffee_types:
        item: CoffeeCrawlerItem = CoffeeCrawlerItem()
        item["coffee_name"] = coffee.css(
            ".nv-card-content-wrapper .woocommerce-loop-product__title::text"
        ).get()
        item["coffee_price"] = (
            coffee.css('[class="nv-card-content-wrapper"]')
            .css('[class="price"]')
            .css("::text")
            .get()
        )
        item["coffee_image"] = coffee.css(
            ".nv-card-content-wrapper .img-wrap img::attr(src)"
        ).get()

        yield item
