# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PersonInfo(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    salary = scrapy.Field()
    phone = scrapy.Field()


class BlogItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    post_time = scrapy.Field()
    modified_time = scrapy.Field()
    file_count = scrapy.Field()
    tags = scrapy.Field()
    detail = scrapy.Field()
