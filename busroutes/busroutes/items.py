# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class RouteItem(Item):
	name = Field()
	origin = Field()
	destination = Field()
	first_up = Field()
	last_up = Field()
	first_down = Field()
	last_down = Field()
	frequency = Field()

class RouteInfoItem(Item):
	name = Field()
	stops = Field()
	
class RouteStopItem(Item):
	number = Field()
	stop = Field()

class StopItem(Item):
	name = Field()