# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from dresslily_scrap.utils.regex_patterns import PRODUCT_INFO_REG


class HoodiesScraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        adapter["product_info"] = ";".join(
            f"{k.strip()}:{v.strip()}"
            for k, v in PRODUCT_INFO_REG.findall(adapter.get("product_info"))
        )

        # all numeric must be zero if None
        for field in ["discount", "discounted_price", "total_reviews"]:
            if adapter[field] is None:
                adapter[field] = 0

        return item
