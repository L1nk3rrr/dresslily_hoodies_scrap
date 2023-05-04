# Scrapy settings for Dresslily project

BOT_NAME = "Dresslily"

SPIDER_MODULES = ["dresslily_scrap.spiders"]
NEWSPIDER_MODULE = "dresslily_scrap.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
   "dresslily_scrap.middlewares.CustomUserAgentMiddleware": 543,
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
