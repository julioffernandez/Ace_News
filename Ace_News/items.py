import scrapy

class CrawlerItem(scrapy.item):
	url = scrapy.Field()
	html = scrapy.Field()