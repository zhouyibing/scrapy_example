import scrapy

from scrapy_test.items import PersonInfo


class PersonInfoSpider(scrapy.Spider):
    name = "person_info_spider"
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ["http://exercise.kingname.info/exercise_xpath_3.html"]

    def parse(self, response):
        person_list = response.xpath('//div[@class="person_table"]/table/tbody/tr')
        for person in person_list:
            item = PersonInfo()
            person_info = person.xpath('./td/text()').extract()
            item['name'] = person_info[0]
            item['age'] = person_info[1]
            item['salary'] = person_info[2]
            item['phone'] = person_info[3]
            print("person info: ", item)
            yield item
