import math
import json

import scrapy

from dresslily_scrap.locators import NEXT_PAGE, HOODIE, HOODIES_LINK, TOTAL_REVIEWS
from dresslily_scrap.items import ReviewItem
from dresslily_scrap.utils.regex_patterns import PRODUCT_ID_REG


class ReviewsSpider(scrapy.Spider):
    name = "reviewsspider"
    allowed_domains = ["www.dresslily.com"]
    base_url = "https://www.dresslily.com"
    start_urls = ["https://www.dresslily.com/hoodies-c-181.html"]

    custom_settings = {
        "FEEDS": {
            "../scraped_data/%(name)s_%(time)s.csv": {"format": "csv", }
        }
    }
    review_headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "x-requested-with": "XMLHttpRequest",
    }

    def parse(self, response):
        hoodies = response.css(HOODIE)
        for hoodie in hoodies:
            hoodie_link = hoodie.css(HOODIES_LINK)
            yield response.follow(hoodie_link.get(), callback=self.parse)
        next_global_page = response.xpath(NEXT_PAGE).get()

        total_reviews = response.css(TOTAL_REVIEWS).get()
        if total_reviews is not None:
            pages_amount = math.ceil(int(total_reviews) / 4)  # if 1/4 would be 1
            product_id = PRODUCT_ID_REG.search(response.url).group(1)
            for page in range(1, pages_amount + 1):
                url = f"https://www.dresslily.com/m-review-a-view_review_list-goods_id-{product_id}-page-{page}?odr=0"
                yield response.follow(url, callback=self.parse_item, headers=self.review_headers)

        if next_global_page is not None:
            next_global_page_url = self.base_url + next_global_page
            yield response.follow(next_global_page_url, callback=self.parse)

    def parse_item(self, response):
        body = json.loads(response.body)
        for review in body["data"]["review"]["review_list"]:
            review_item = ReviewItem(
                product_id=review["goods_id"],
                rating=review["rate_overall"],
                timestamp=review["adddate"],
                text=review["pros"],
                size=review.get("goods", {}).get("size"),
                color=review.get("goods", {}).get("color"),
            )
            yield review_item

