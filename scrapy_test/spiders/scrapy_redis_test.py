from scrapy_redis.spiders import RedisSpider


class ScrapyRedisTestSpider(RedisSpider):
    name = 'scrapy_redis_test'
    redis_key = 'scrapy_redis_test:start_urls'

    def parse(self, response):
        print(response.url)
        print(response.text)
        pass