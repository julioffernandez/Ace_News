import scrapy

class MatchesItem(scrapy.item):
	url = Field()
	equipo_1 = Field()
    equipo_2 = Field()
    set_1_equipo_1 = Field()
    set_1_equipo_2 = Field()
    set_2_equipo_1 = Field()
    set_2_equipo_2 = Field()
    set_3_equipo_1 = Field()
    set_3_equipo_2 = Field()
    set_4_equipo_1 = Field()
    set_4_equipo_2 = Field()
    set_5_equipo_1 = Field()
    set_5_equipo_2 = Field()