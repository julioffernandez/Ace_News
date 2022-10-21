from scrapy import Spider, Request
from Ace_News.items import MatchesItem
from bs4 import BeautifulSoup

class Tenispider(Spider):
	name = "TenisSpider"
	allowed_url=["https://www.xscores.com/tennis"]

	def start_requests(self):
		urls = ['https://www.xscores.com/tennis']
		for url in urls:
			yield Request(url=url, callback=self.parse)


	#Parsear cada objeto partido de la página
	def parse(self,response):
		half_matches_urls = response.xpath('//*[@id="scoretable"]//a[@class="match_line score_row other_match"]/@href').extract()
		matchurl="https://www.xscores.com/tennis/match/"
		#list comprehension to concat domain with sublinks in half_watches_urls
		res=[matchurl+s for s in half_matches_urls]
		for url in res:
			yield Request(url=url, callback=self.parse_match_page)

	#Cada atributo de cada partido se define aquí
	def parse_match_page(self,response):

		item=MatchesItem()
		item["url"]=" "
		#item["url"]=self.url response.xpath('//script[@rel="bmc-data"]').re('homeTeam": "(.+)"')
		# soup.find_all("homeTeam")
		item["equipo_1"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div/div[3]/div/div/div[2]/div[1]/text()').get()
		item["equipo_2"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div/div[3]/div/div/div[3]/div[1]/text()').get()
		item["set_1_equipo_1"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[2]/div[3]/text()').get()
		item["set_1_equipo_2"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[3]/div[3]/text()').get()
		item["set_2_equipo_1"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[2]/div[4]/text()').get()
		item["set_2_equipo_2"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[3]/div[4]/text()').get()
		item["set_3_equipo_1"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[2]/div[5]/text()').get()
		item["set_3_equipo_2"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[3]/div[5]/text()').get()
		item["set_4_equipo_1"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[2]/div[6]/text()').get()
		item["set_4_equipo_2"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[3]/div[6]/text()').get()
		item["set_5_equipo_1"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[2]/div[7]/text()').get()
		item["set_5_equipo_2"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[3]/div[7]/text()').get()

		yield item