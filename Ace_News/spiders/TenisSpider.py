from scrapy import Spider, Request

class Tenispider(Spider):
	name = "TenisSpider"
	allowed_url=["https://www.xscores.com/tennis"]

	def start_requests(self):
		urls = ['https://www.xscores.com/tennis']
		for url in urls:
			yield Request(url=url, callback=self.parse)

	#Parsear cada objeto partido de la página
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

        item=MatchesItem()
        item["url"]=" "
        #item["url"]=self.url 
        item["equipo_1"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div/div[3]/div/div/div[2]/div[1]').extract()
        item["equipo_2"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div/div[3]/div/div/div[3]/div[1]').extract()
        item["set_1_equipo_1"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[2]/div[3]').extract()
        item["set_1_equipo_2"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[3]/div[3]').extract()
        item["set_2_equipo_1"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[2]/div[4]').extract()
        item["set_2_equipo_2"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[3]/div[4]').extract()
        item["set_3_equipo_1"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[2]/div[5]').extract()
        item["set_3_equipo_2"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[3]/div[5]').extract()
        item["set_4_equipo_1"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[2]/div[6]').extract()
        item["set_4_equipo_2"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[3]/div[6]').extract()
        item["set_5_equipo_1"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[2]/div[7]').extract()
        item["set_5_equipo_2"]=response.xpath('/html/body/div[8]/div[2]/div[7]/div[3]/div[2]/div/div/div[6]/div[1]/div[1]/div/div/div[3]/div[7]').extract()

        yield item