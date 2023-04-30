import scrapy

from dresslily_scrap.locators import NEXT_PAGE, HOODIES_LINKS


class HoodiesspiderSpider(scrapy.Spider):
    name = "hoodiesspider"
    allowed_domains = ["dresslily.com"]
    base_url = "https://www.dresslily.com"
    start_urls = ["https://www.dresslily.com/hoodies-c-181.html"]

    def parse(self, response):
        hoodies = response.css(HOODIES_LINKS)
        for hoodie in hoodies:
            print(hoodie)
            yield response.follow(hoodie.get(), callback=self.parse_item)

        next_page = response.xpath(NEXT_PAGE).get()
        if next_page is not None:
            next_page_url = self.base_url + next_page
            yield response.follow(next_page_url, callback=self.parse)

    def parse_item(self, response):
        pass