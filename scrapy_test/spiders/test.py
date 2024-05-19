import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["baidu.com","exercise.kingname.info"]
    start_urls = ["https://baidu.com", "http://exercise.kingname.info/exercise_xpath_1.html","http://exercise.kingname.info/exercise_xpath_2.html"]

    def parse(self, response):
        # print(response.body.decode())
        if "baidu.com" in response.url:
            self.test1(response)
            self.test2(response)
        elif "exercise_xpath_1" in response.url:
            self.exercise_test(response)
        elif "exercise_xpath_2" in response.url:
            self.exercise_test2(response)

    def test1(self, response):
        print("----------test1---------")
        title = response.xpath("//title/text()").extract()
        search_btn_txt = response.xpath("//input[@class='bg s_btn']/@value").extract()
        # print(response.body.decode())
        print(title)
        print(search_btn_txt)

    def test2(self, response):
        print("----------test2---------")
        title_example = response.xpath("//title/text()")
        title_example_1 = title_example.extract()[0]
        title_example_2 = title_example[0].extract()
        print(title_example_1)
        print(title_example_2)
        print(title_example.extract_first())

    def exercise_test(self, response):
        print('----------exercise_test---------')
        name_list = response.xpath('//li[@class="name"]/text()').extract()
        price_list = response.xpath('//li[@class="price"]/text()').extract()
        for i in range(len(name_list)):
            print("商品：{}，价格：{}".format(name_list[i], price_list[i]))

    def exercise_test2(self, response):
        print('----------exercise_test2---------')
        item_list = response.xpath('//ul[@class="item"]')
        for item in item_list:
            name = item.xpath('./li[@class="name"]/text()').extract()
            price = item.xpath('./li[@class="price"]/text()').extract()
            name = name[0] if name else 'N/A'
            price = price[0] if price else 'N/A'
            print("商品：{}，价格：{}".format(name, price))
