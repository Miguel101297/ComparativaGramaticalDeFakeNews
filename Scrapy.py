import scrapy
from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import Join
from bs4 import BeautifulSoup

class LeMondeItem(Item):
    titulo = Field()
    contenido = Field()

class LeMondeCrawler(CrawlSpider):
    name = 'ejemplo'
    allowed_domains = ['haynoticias']
    start_urls = ['ejemplo']

    rules = (
        Rule(LinkExtractor(allow=r'/ejemplo/\d+'), follow=True),
        Rule(LinkExtractor(allow=r'/ejemplo'), follow=True, callback='parse_items'),
    )

    def parse_items(self, response):
        item = scrapy.loader.ItemLoader(LeMondeItem(), response)
        item.add_xpath('titulo', '//h1/text()')

        soup = BeautifulSoup(response.body)
        article = soup.find(id="articleBody")
        contenido = article.text.replace('\n', ' ').replace('\r', ' ')
        item.add_value('contenido', contenido)

        yield item.load_item()
