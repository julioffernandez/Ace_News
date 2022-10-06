from scrapy import Spider, Request

class Tenispider(Spider):
	name = "TenisSpider"

	def start_requests(self):
		urls = ['https://www.xscores.com/tennis']
		for url in urls:
			yield Request(url=url, callback=self.parse)


	def parse(self, response, **kwargs):
		page = response.url
		print(page)