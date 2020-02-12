import scrapy


class LegoItem(scrapy.Item):
    model = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    rating = scrapy.Field()
    available = scrapy.Field()
    pass
