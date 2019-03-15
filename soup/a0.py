# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class A0Spider(CrawlSpider):
    name = '0'
    allowed_domains = ['http://www.skybet.com/horse-racing']
    start_urls = ['http://http://www.skybet.com/horse-racing/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
