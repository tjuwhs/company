# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class ZhiQiYeSpider(scrapy.Spider):
    name = "zhiqiye"
    allowed_domains = ["zhiqiye.com"]
    start_urls = (
        'http://www.zhiqiye.com/search/list?kwd=上海巨人网络科技有限公司&sType=1',
    )

    def parse(self, response):
        print response.selector.css('.seach-result').xpath("(./ul/li)[1]").extract()
