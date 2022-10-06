from itemadapter import ItemAdapter


class CrawlerPipeline:
    def process_item(self, item, spider):
        if isinstance(item, CrawlerItem):
            url: str = item['url']
            html: bytes = item['html']
            page_slug: str = get_organization_slug_from_url(url)
            page_domain: str = spider.allowed_domains[0]
            path_to_save: str = SAVE_PATH.format(page_domain)

            save_into_html(html, path_to_save, f"{page_domain}-{page_slug}")

        return item


    ITEM_PIPELINES = {
        'focused_crawler.pipelines.SaveCrawlerItem': 300,
    }
