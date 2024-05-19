from html import unescape

import scrapy
from lxml import etree
from scrapy_redis.spiders import RedisSpider

from scrapy_test.items import BlogItem


class BlogSpider(RedisSpider):
    name = 'blog_crawler'
    redis_key = 'blog_crawler'
    allowed_domains = ['www.kingname.info']
    # 代码中配置start_urls是无效的，需要在redis中配置redis_key并加入这个url
    start_urls = ['https://www.kingname.info']
    host = "https://www.kingname.info"

    def parse(self, response):
        title_tag_list = response.xpath('//a[@class="post-title-link"]')
        for title_tag in title_tag_list:
            article_title = title_tag.xpath('span/text()').extract_first()
            article_url = self.host + title_tag.xpath('@href').extract_first()
            blog_item = BlogItem()
            blog_item['title'] = article_title
            blog_item['url'] = article_url
            print("article_title={},article_url={}".format(article_title, article_url))
            yield scrapy.Request(article_url, callback=self.parse_detail, meta={'blog_item': blog_item})

    def parse_detail(self, response):
        print("parse_detail:{}".format(response.url))
        blog_item = response.meta['blog_item']
        blog_item['post_time'] = response.xpath('//time[@itemprop="dateCreated datePublished"]/@datetime').extract_first()
        blog_item['modified_time'] = response.xpath('//time[@itemprop="dateModified"]/@datetime').extract_first()
        # not(@class) 表示不包含class属性
        blog_item['file_count'] = response.xpath('//span[@class="post-meta-item"][@title="本文字数"]/span[not(@class)]/text()').extract_first()
        blog_item['tags'] = response.xpath('//div[@class="post-tags"]/a/text()').extract()
        post_body = response.xpath('//div[@class="post-body"]')
        blog_item['detail'] = unescape(etree.tostring(post_body[0].root, encoding='utf-8').decode())
        print("fetch article detail sucessful, detail:{}".format(blog_item))
        yield blog_item
