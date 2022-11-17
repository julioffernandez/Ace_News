import scrapy
from Ace_News.items import ArticlesItem
from scrapy import Spider, Request


class PuntobreakSpider(scrapy.Spider):
    name = 'puntobreak'
    allowed_domains = ['www.puntodebreak.com']
    start_urls = []
    i=0
    for i in range(16):
        start_urls.append('https://www.puntodebreak.com/archivo?page='+str(i))

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)


    def parse(self, response):
        stories = []
        item=ArticlesItem()

        results = response.xpath('//div[has-class("md-article-item-list node node-embed node-promoted view-mode-md_basic_page_list")] | //div[has-class("md-article-item-list node node-story node-promoted view-mode-md_basic_page_list")]')
        
        for result in results:
            extraction = ""
            
            if result.xpath('.//p[has-class("rtejustify")]/span/text()').get() is None:
                explainnormaltext = result.xpath('.//p[has-class("rtejustify")]/text() | .//p[has-class("rtejustify")]/strong/text() | .//p[has-class("rtejustify")]/a/strong/text()').getall()
                for text in explainnormaltext:
                    extraction = extraction + text
            else:
                extraction = result.xpath('.//p[has-class("rtejustify")]/span/text()').get()
            item["url"] = 'https://www.puntodebreak.com' + result.xpath('./h2/a/@href').get()
            item["title"] = result.xpath('./h2/a/text()').get()
            item["extract"] = extraction
            item["image"] = result.xpath('.//img[has-class("media-o-h")]/@src').get()
            item["time"] = result.xpath('./div[has-class("md-article-info")]/time/a/text() | ./div[has-class("md-article-info")]/time/text()').get()
            item["tags"] = result.xpath('./div[has-class("md-article-info")]/span/a/li/a/text() | ./div[has-class("md-article-info")]/span/li/a/text()').getall()
            yield item
