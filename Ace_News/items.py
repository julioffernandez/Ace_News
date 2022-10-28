import scrapy

class MatchesItem(scrapy.Item):
	url = scrapy.Field()
	equipo_1 = scrapy.Field()
	equipo_2 = scrapy.Field()
	set_1_equipo_1 = scrapy.Field()
	set_1_equipo_2 = scrapy.Field()
	set_2_equipo_1 = scrapy.Field()
	set_2_equipo_2 = scrapy.Field()
	set_3_equipo_1 = scrapy.Field()
	set_3_equipo_2 = scrapy.Field()
	set_4_equipo_1 = scrapy.Field()
	set_4_equipo_2 = scrapy.Field()
	set_5_equipo_1 = scrapy.Field()
	set_5_equipo_2 = scrapy.Field()
	resultadofinal_1 = scrapy.Field()
	resultadofinal_2 = scrapy.Field()