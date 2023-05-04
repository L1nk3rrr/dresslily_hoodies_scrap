# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import time

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


class ReviewItem(scrapy.Item):
    product_id = scrapy.Field()
    rating = scrapy.Field()
    timestamp = scrapy.Field(serializer=lambda value: int(time.mktime(time.strptime(value, "%b,%d %Y %H:%M:%S"))))
    text = scrapy.Field()
    size = scrapy.Field()
    color = scrapy.Field()
