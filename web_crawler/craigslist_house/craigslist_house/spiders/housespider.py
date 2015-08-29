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
        contents = hxs.xpath("//div[@class='content']/*")
        titles=context.xpath("//p/span/span/a/text()").extract()
        urls=context.xpath("//p/span/span[@class='pl']/a/@href").extract()
        prices=context.xpath("//p/span/span[@class='l2']/span[@class='price']/text()").extract()
        print "hehe"
        print (titles,urls,prices)
#        for context in contents:
#            item=CraigslistHouseItem()
#            item["title"]=context.xpath("//p/span/span/a/text()").extract()
#            item["url"]=httpHead+context.xpath("//p/span/span[@class='pl']/a/@href").extract()[0]
#            item["price"]=context.xpath("//p/span/span[@class='l2']/span[@class='price']/text()").extract()
#            items.append(item)
        return(items)
