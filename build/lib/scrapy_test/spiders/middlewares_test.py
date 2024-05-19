import scrapy


class MiddlewaresSpider(scrapy.Spider):
    name = 'middlewares_test'
    allowed_domains = ['exercise.kingname.info']
    start_urls = ['https://exercise.kingname.info/exercise_middleware_ip', 'http://exercise.kingname.info/exercise_login_success']

    def parse(self, response):
        print(response.body.decode())
