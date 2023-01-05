import scrapy


class UnionmangaSpider(scrapy.Spider):
    name = 'unionmanga'
    allowed_domains = ['unionmanga.com']
    start_urls = ['https://unionleitor.top/leitor/One_Piece/1071']

    def parse(self, response):
        raw_image_urls = response.css('.img-manga::attr(src)').getall()

        clean_image_urls = []
        #clean_image_urls as List
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url)) #qualquer url fornecida dentro disso como um parâmetro. será convertida em url absoluto evita o erro %20

        yield{
            'image_urls': clean_image_urls,
        }