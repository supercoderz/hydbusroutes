from scrapy.spider import Spider
from scrapy.selector import Selector

class SimpleRouteSpider(Spider):
	name = "simpleroute"
	allowed_domains = ["hyderabadbusroutes.com"]

	def parse(self, response):
		sel = Selector(response)
		routes = sel.xpath('//table/tr')
		for route in routes:
			print route.xpath('.//text()').extract()
			
	def start_requests(self):
		urls=[]
		base='http://www.hyderabadbusroutes.com/index.php?service=BUSROUTE&page='
		for i in range(1,30):
			urls.append(base+str(i))
		return [self.make_requests_from_url(url) for url in urls]
