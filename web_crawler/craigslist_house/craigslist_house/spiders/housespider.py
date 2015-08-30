from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from craigslist_house.items import CraigslistHouseItem

httpHead="https://losangeles.craigslist.org"
class HouseSpiders(Spider):
    name = "crawl_house"
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://losangeles.craigslist.org/search/apa?sort=date"]
   # httpHead="https://losangeles.craigslist.org/"
   # rules=(Rule (SgmlLinkExtractor(allow=("index\d00\.html", ),restrict_xpaths=('//a[@class="button next"]',))
   # , callback="parse_items", follow= True), )

    def parse(self, response):
        items=[]
        hxs=Selector(response)
        contexts = hxs.xpath("//div[@class='content']/p[@class='row']")
        for context in contexts:
            item=CraigslistHouseItem()
            item["title"]=context.xpath("//p/span/span[@class='pl']/a/text()").extract()
            item["url"]=context.xpath("//p/span/span[@class='pl']/a/@href").extract()
            item["price"]=context.xpath("//p/span/span[@class='l2']/span[@class='price']/text()").extract()
            items.append(item)
        return(items)
