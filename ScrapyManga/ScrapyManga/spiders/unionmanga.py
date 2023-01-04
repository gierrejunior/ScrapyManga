import scrapy


class UnionmangaSpider(scrapy.Spider):
    name = 'unionmanga'
    allowed_domains = ['unionmanga.com']
    start_urls = ['http://unionmanga.com/']

    def parse(self, response):
        pass
