from itemadapter import ItemAdapter
from Ace_News.items import MatchesItem, ArticlesItem
import json


class Ace_NewsPipeline:

    def open_spider(self, spider):
        self.file = open('items.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        parsed_item = {}
        if isinstance(item, MatchesItem):
            parsed_item["url"]: str = item['url']
            parsed_item["equipo_1"]: str = item['equipo_1']
            parsed_item["equipo_2"]: str = item['equipo_2']
            parsed_item["set_1_equipo_1"]: int = int(item['set_1_equipo_1']) if item['set_1_equipo_1'] != "-" else None
            parsed_item["set_1_equipo_2"]: int = int(item['set_1_equipo_2']) if item['set_1_equipo_2'] != "-" else None
            parsed_item["set_2_equipo_1"]: int = int(item['set_2_equipo_1']) if item['set_2_equipo_1'] != "-" else None
            parsed_item["set_2_equipo_2"]: int = int(item['set_2_equipo_2']) if item['set_2_equipo_2'] != "-" else None
            parsed_item["set_3_equipo_1"]: int = int(item['set_3_equipo_1']) if item['set_3_equipo_1'] != "-" else None
            parsed_item["set_3_equipo_2"]: int = int(item['set_3_equipo_2']) if item['set_3_equipo_2'] != "-" else None
            parsed_item["set_4_equipo_1"]: int = int(item['set_4_equipo_1']) if item['set_4_equipo_1'] != "-" else None
            parsed_item["set_4_equipo_2"]: int = int(item['set_4_equipo_2']) if item['set_4_equipo_2'] != "-" else None
            parsed_item["set_5_equipo_1"]: int = int(item['set_5_equipo_1']) if item['set_5_equipo_1'] != "-" else None
            parsed_item["set_5_equipo_2"]: int = int(item['set_5_equipo_2']) if item['set_5_equipo_2'] != "-" else None
            parsed_item["resultadofinal_1"]: int = int(item['resultadofinal_1']) if item['resultadofinal_1'] != "-" else None
            parsed_item["resultadofinal_2"]: int = int(item['resultadofinal_2']) if item['resultadofinal_2'] != "-" else None
        else:
            if isinstance(item, ArticlesItem):
                parsed_item["url"]: str = item['url']
                parsed_item["title"]: str = item["title"]
                parsed_item["v"]: str = item["extract"]
                parsed_item["image"]: str = item["image"]
                parsed_item["time"]: str = item["time"]
                parsed_item["tags"]: str = item["tags"]
        line = json.dumps(parsed_item, ensure_ascii=False) + "\n"
        self.file.write(line)            
        return item


    ITEM_PIPELINES = {
        'focused_crawler.pipelines.SaveCrawlerItem': 300,
    }
