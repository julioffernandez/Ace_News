import scrapy


class PuntobreakSpider(scrapy.Spider):
    name = 'puntobreak'
    allowed_domains = ['www.puntodebreak.com']
    start_urls = ['https://www.puntodebreak.com']

    def parse(self, response):
        stories = []

        results = response.xpath('//div[has-class("node-story")]')
        
        for result in results:
            
            title = result.xpath('./h2/a/text()').get()
            extract = result.xpath('.//p[has-class("rtejustify")]/text()').get()
            image = result.xpath('.//img[has-class("media-o-h")]/@src').get()
            time = result.xpath('./div[has-class("md-article-info")]/time/text()').get()
            tags = result.xpath('./div[has-class("md-article-info")]/span/a/text()').getall()

            story = [
                    {"title": title},
                    {"extract": extract},
                    {"image": image},
                    {"time": time},
                    {"tags": tags},
                    ]

            stories.append(story)
        
        yield {
            'stories': stories,
        }
