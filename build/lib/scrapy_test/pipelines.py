# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import redis
from scrapy.utils.project import get_project_settings
settings = get_project_settings()


class ScrapyTestPipeline:
    def process_item(self, item, spider):
        # print("process_item item: ", item)
        return item


class RedisPipeline:
    def __init__(self):
        host = settings['REDIS_HOST']
        port = settings['REDIS_PORT']
        pwd = settings['REDIS_PASS']
        db = settings['REDIS_DB']
        # self.redis_client = redis.StrictRedis(host=host, port=port, db=db, password=pwd)
        # self.redis_client.set("test", "test")

    def process_item(self, item, spider):
        person_info = dict(item)
        print("RedisPipeline person_info: ", person_info)
        # person_info转为字符串
        self.redis_client.set("user:" + person_info['name'], str(person_info))
        return item


class BlogPipeline:
    def __init__(self):
        host = settings['REDIS_HOST']
        port = settings['REDIS_PORT']
        pwd = settings['REDIS_PASS']
        db = settings['REDIS_DB']
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db, password=pwd)
        self.redis_client.set("test", "test")

    def process_item(self, item, spider):
        blog_info = dict(item)
        print("BlogPipeline blog_info: ", blog_info)
        self.redis_client.set("blog:" + blog_info["url"], str(blog_info))
        return item