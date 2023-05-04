# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    product_id = scrapy.Field()
    product_url = scrapy.Field()
    name = scrapy.Field()
    discount = scrapy.Field()
    discounted_price = scrapy.Field()
    original_price = scrapy.Field()
    total_reviews = scrapy.Field()
    product_info = scrapy.Field()
