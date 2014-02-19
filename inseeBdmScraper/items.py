# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class InseeItem(Item):
    idBank = Field()
    series_info = Field()
    year = Field()
    month = Field()
    values = Field()