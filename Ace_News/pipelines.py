from itemadapter import ItemAdapter
from Ace_News.items import MatchesItem
import json


class Ace_NewsPipeline:

    def open_spider(self, spider):
        self.file = open('items.jsonl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, MatchesItem):
            url: str = item['url']
            equipo_1: str = item['equipo_1']
            equipo_2: str = item['equipo_2']
            set_1_equipo_1: str = item['set_1_equipo_1']
            set_1_equipo_2: str = item['set_1_equipo_2']
            set_2_equipo_1: str = item['set_2_equipo_1']
            set_2_equipo_2: str = item['set_2_equipo_2']
            set_3_equipo_1: str = item['set_3_equipo_1']
            set_3_equipo_2: str = item['set_3_equipo_2']
            set_4_equipo_1: str = item['set_4_equipo_1']
            set_4_equipo_2: str = item['set_4_equipo_2']
            set_5_equipo_1: str = item['set_5_equipo_1']
            set_5_equipo_2: str = item['set_5_equipo_2']

        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)            
        return item


    ITEM_PIPELINES = {
        'focused_crawler.pipelines.SaveCrawlerItem': 300,
    }
