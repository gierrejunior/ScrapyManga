import scrapy


class MangalivreSpider(scrapy.Spider):
    name = 'mangalivre'
    allowed_domains = ['mangalivre.com']
    start_urls = ['https://mangalivre.net/ler/one-piece/online/432114/1071#/!page0']

    def parse(self, response):
        pass
