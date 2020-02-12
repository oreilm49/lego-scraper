# -*- coding: utf-8 -*-
from scrapy import Spider
#from scrapy.selector import Selector
from scraper.items import LegoItem
import string
import re


class LegoSpider(Spider):
    name = 'lego'
    allowed_domains = ['lego.com']
    start_urls = ['https://www.lego.com/en-ie/themes/disney-frozen-2']

    def parse(self, response):
        products =  response.css(
            "[data-test='product-item'] > div > div > a::attr(href)"
        )
        pagination = response.css("a[data-test='pagination-next']::attr(href)")

        for href in products:
            yield response.follow(href, self.parse_product)

        for href in pagination:
            yield response.follow(href, self.parse)


    def parse_product(self, response):
        model = response.css(
                    'meta[property="product:retailer_item_id"]::attr(content)'
                ).extract_first()
        name = response.css(
                    "h1[data-test='product-overview-name'] > span::text"
                ).extract_first()
        price = response.css(
                    "span[data-test='product-price']::text"
                ).extract_first()
        description = response.css((
                    'div[data-test="product-accordion-specifications'
                    '-content"] p::text'
                )).extract_first()
        available = response.css((
                    'p[data-test="product-overview-availability"]'
                    ' span::text'
                )).extract_first()
        rating = response.css((
                    'div[class*="ProductOverviewstyles"] '
                    'div[class*="RatingBar__RatingContainer"]'
                    '::attr(title)'
                )).extract_first()
        item = LegoItem()
        item['model'] = model
        item['name'] = name
        item['price'] = price
        item['description'] = description
        item['available'] = available
        item['rating'] = rating
        yield item
