from scrapy import Spider, Request

class Tenispider(Spider):
	name = "TenisSpider"
	allowed_url=["https://www.xscores.com/tennis"]

	def start_requests(self):
		urls = ['https://www.xscores.com/tennis']
		for url in urls:
			yield Request(url=url, callback=self.parse)

	#Parsearr cada objeto partido de la página
	def parse(self, response):
		#matches info
        half_matches_urls = response.xpath('//div[@class="match_line score_row other_match"]/a/@href').extract()
        matchurl="https://www.xscores.com/tennis/match/"
        #list comprehension to concat domain with sublinks in half_watches_urls
        res=[matchurl+s for s in half_matches_urls]
        for url in res:
            yield Request(url=url, callback=self.parse_match_page)

    #Cada atributo de cada partido se define aquí
    def parse_match_page(self,response):
        product = response.xpath('//h1[@class="table_div_in"]/text()').extract()
        item_number=response.xpath('//span[@itemprop="sku"]/text()').extract()
        retail_price=response.xpath('//span[@id="pitPriceBx"]/text()').extract()
        price=response.xpath('//span[@id="pitSalePriceBx"]/text()').extract()
        availability=response.xpath('//span[@class="availability"]/text()').extract()
        condition=response.xpath('//select[@name="Condition"]/option/@value').extract()
        warranty=response.xpath('//select[@name="Warranty"]/option/@value').extract()
        image=response.xpath('//div[@class="itemimg"]/div/a/@href').extract_first()

        item=AuthenticwatchesItem()
        item["product"]=product
        item["item_number"]=item_number
        item["retail_price"]=retail_price
        item["price"]=price
        item["availability"]=availability
        item["condition"]=condition
        item["warranty"]=warranty
        item["image"]=image

        yield item