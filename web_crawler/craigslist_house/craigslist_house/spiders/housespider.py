from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from craigslist_house.items import CraigslistHouseItem
from scrapy.linkextractors import LinkExtractor

httpHead="https://losangeles.craigslist.org"
class HouseSpiders(CrawlSpider):
    name = "crawl_house"
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://losangeles.craigslist.org/search/apa?sort=date"]
    rules = (Rule(LinkExtractor(restrict_xpaths=('//a[@class="button next"]',)),callback='parse_items', follow= True),)

    def parse_items(self, response):
        items=[]
        hxs = Selector(response)
        #titles = hxs.xpath("//span[@class='pl']")
        #prices = hxs.xpath("//span[@class='l2']")
        contents=hxs.xpath("//span[@class='txt']")
        items = []
        for content in contents:
            item = CraigslistHouseItem()
            item ["title"] = content.select("span[2]/a/text()").extract()
            item ["url"] = httpHead+content.select("span[2]/a/@href").extract()[0]
            item ["price"]=content.select("span[3]/span[1]/text()").extract()
            items.append(item)
        return items
