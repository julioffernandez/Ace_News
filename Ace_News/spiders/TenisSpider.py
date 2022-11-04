from scrapy import Spider, Request
from Ace_News.items import MatchesItem
from bs4 import BeautifulSoup

class Tenispider(Spider):
	name = "TenisSpider"
	allowed_url=["https://www.xscores.com/tennis/finished-games"]

	def start_requests(self):
		urls = ['https://www.xscores.com/tennis/finished-games']
		for url in urls:
			yield Request(url=url, callback=self.parse)


	#Parsear cada objeto partido de la página
	def parse(self,response):
		matcheslinks = response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]').getall()
		i=0
		aux1 = 0
		aux2 = 0
		for matches in matcheslinks:
			item=MatchesItem()
			item["url"]='https://www.xscores.com' + response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/@href').getall()[i]
			team1 = response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[5]/div[1]/div[2]/span/text() | /html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[5]/div[1]/div[2]/span/b/text()').getall()[i+aux1]
			team2 = response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[5]/div[2]/div[2]/span/text() | /html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[5]/div[2]/div[2]/span/b/text()').getall()[i+aux2]
			while(team1 == "Walkover" or team1 == "Retired"):
				aux1=aux1+1
				team1 = response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[5]/div[1]/div[2]/span/text() | /html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[5]/div[1]/div[2]/span/b/text()').getall()[i+aux1]
			item["equipo_1"]= team1
			while(team2 == "Walkover" or team2 == "Retired"):
				aux2=aux2+1
				team2 = response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[5]/div[2]/div[2]/span/text() | /html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[5]/div[2]/div[2]/span/b/text()').getall()[i+aux2]
			item["equipo_2"]= team2
			item["set_1_equipo_1"]=response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[8]/div[1]/text()').getall()[i]
			item["set_1_equipo_2"]=response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[8]/div[2]/text()').getall()[i]
			item["set_2_equipo_1"]=response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[9]/div[1]/text()').getall()[i]
			item["set_2_equipo_2"]=response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[9]/div[2]/text()').getall()[i]
			item["set_3_equipo_1"]=response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[10]/div[1]/text()').getall()[i]
			item["set_3_equipo_2"]=response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[10]/div[2]/text()').getall()[i]
			item["set_4_equipo_1"]=response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[11]/div[1]/text()').getall()[i]
			item["set_4_equipo_2"]=response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[11]/div[2]/text()').getall()[i]
			item["set_5_equipo_1"]=response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[12]/div[1]/text()').getall()[i]
			item["set_5_equipo_2"]=response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[12]/div[2]/text()').getall()[i]
			item["resultadofinal_1"] =response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[13]/div[1]/text()').getall()[i]
			item["resultadofinal_2"] =response.xpath('/html/body/div[6]/div[2]/div[7]/div[5]/div[2]/div[1]//a[@class="match_line score_row other_match"]/div[13]/div[2]/text()').getall()[i]
			i=i+1
			yield item