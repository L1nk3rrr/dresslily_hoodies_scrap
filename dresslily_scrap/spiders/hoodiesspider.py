import scrapy

from dresslily_scrap.locators import (
    NEXT_PAGE, HOODIE, HOODIES_LINK, PRODUCT_NAME, DISCOUNT, DISCOUNT_PRICE, PRODUCT_PRICE, TOTAL_REVIEWS
)
from dresslily_scrap.items import ProductItem
from dresslily_scrap.utils.regex_patterns import PRODUCT_ID_REG


class HoodiesSpider(scrapy.Spider):
    name = "hoodiesspider"
    allowed_domains = ["dresslily.com"]
    base_url = "https://www.dresslily.com"
    start_urls = ["https://www.dresslily.com/hoodies-c-181.html"]

    custom_settings = {
        "ITEM_PIPELINES": {
            'dresslily_scrap.pipelines.HoodiesScraperPipeline': 300
        },
        "FEEDS": {
            "../scraped_data/%(name)s_%(time)s.csv": {"format": "csv", }
        }
    }

    def parse(self, response):
        hoodies = response.css(HOODIE)
        for hoodie in hoodies:
            hoodie_link = hoodie.css(HOODIES_LINK)
            # getting price info here due to dynamic js script is slow at the product page
            kwargs = {
                "discount": hoodie.css(DISCOUNT).get(),
                "discount_price": hoodie.css(DISCOUNT_PRICE).get(),
                "original_price": hoodie.css(PRODUCT_PRICE).get(),
            }
            yield response.follow(hoodie_link.get(), callback=self.parse_item, cb_kwargs=kwargs)

        next_page = response.xpath(NEXT_PAGE).get()
        if next_page is not None:
            next_page_url = self.base_url + next_page
            yield response.follow(next_page_url, callback=self.parse)

    def parse_item(self, response, discount, discount_price, original_price):
        product_item = ProductItem(
            product_id=PRODUCT_ID_REG.search(response.url).group(1),
            product_url=response.url,
            name=response.css(PRODUCT_NAME).get(),
            discount=discount,
            discounted_price=discount_price,
            original_price=original_price,
            total_reviews=response.css(TOTAL_REVIEWS).get(),
            product_info=response.css(".xxkkk20").get(),
        )
        yield product_item
