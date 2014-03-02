from scrapy.spider import Spider
from scrapy.selector import Selector
from busroutes.items import RouteItem,StopItem,RouteInfoItem,RouteStopItem
import json

class HyderabadRouteSpider(Spider):
	name = "fetchhydroutes"
	allowed_domains = ["hyderabadbusroutes.com"]

	def parse(self, response):
		sel = Selector(response)
		route_names = []
		routes = sel.xpath('//table/tr')
		for route in routes:
			route_data = route.xpath('.//text()').extract()
			print route_data
			route_name = route_data[0]
			route_origin = route_data[1]
			route_destination = route_data[2]
			if route_name!=None and route_name.strip()!='':
				item = RouteItem()
				origin = StopItem()
				origin['name'] = route_origin
				destination = StopItem()
				destination['name'] = route_destination
				item['name'] = route_name
				item['origin'] = origin
				item['destination'] = destination
				item['first_up'] = route_data[3]
				item['last_up'] = route_data[4]
				item['first_down'] = route_data[5]
				item['last_down'] = route_data[6]
				item['frequency'] = route_data[8]
				route_names.append(item)
		return route_names
	
	def start_requests(self):
		urls=[]
		base='http://www.hyderabadbusroutes.com/index.php?service=BUSROUTE&page='
		for i in range(1,30):
			urls.append(base+str(i))
		return [self.make_requests_from_url(url) for url in urls]

class HyderabadRouteInfoSpider(Spider):
	name = "fetchhydrouteinfo"
	allowed_domains = ["hyderabadbusroutes.com"]
	
	def parse(self, response):
		sel = Selector(response)
		index = response.url.rfind("=")+1
		route_name = response.url[index:]
		route_stops = []
		stops = sel.xpath("//table/tr[@class='noborders']")
		for stop in stops:
			stop_data = stop.xpath('.//text()').extract()
			route_stop = RouteStopItem()
			route_stop['number'] = stop_data[0]
			stop_item = StopItem()
			stop_item['name'] = stop_data[1]
			route_stop['stop'] = stop_item
			route_stops.append(route_stop)
		route_info = RouteInfoItem()
		route_info['name'] = route_name
		route_info['stops'] = route_stops
		return route_info
	
	def start_requests(self):
		urls=[]
		json_data = open('hyd_routes.json').read()
		routes = json.loads(json_data)
		base='http://www.hyderabadbusroutes.com/index.php?service=BUSINFO&busno='
		for route in routes:
			urls.append(base+route['name'])
		return [self.make_requests_from_url(url) for url in urls]
