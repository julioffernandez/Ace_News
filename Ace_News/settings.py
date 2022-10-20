# Scrapy settings for Ace_News

BOT_NAME = 'Ace_News'

SPIDER_MODULES = ['Ace_News.spiders']
NEWSPIDER_MODULE = 'Ace_News.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 3

COOKIES_ENABLED = False

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Ace_News.pipelines.Ace_NewsPipeline': 300,
}