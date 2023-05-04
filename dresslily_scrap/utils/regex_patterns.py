import re

PRODUCT_ID_REG = re.compile(r"product(\d+)\.html")
PRODUCT_INFO_REG = re.compile(r"<strong>(.+?):<\/strong>\s*(.*?)<")