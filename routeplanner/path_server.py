import json
import networkx as nx
from itertools import izip
import tornado.ioloop
import tornado.web
import os

dirname = os.path.dirname(__file__)
STATIC_PATH = os.path.join(dirname, 'static')
TEMPLATE_PATH = os.path.join(dirname, 'templates')
graph_builder = None

class GraphBuilder(object):
	def __init__(self):
		self.graph = nx.MultiGraph()

		data_str = open('routes.json').read()
		data = json.loads(data_str)

		for item in data:
			route_name = item['name']
			stops = item['stops']
			stop_names = [stop['stop']['name'] for stop in stops]
			if stop_names!=[]:
				self.graph.add_path(stop_names,route=route_name)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.post()
	
	def post(self):
		origin = self.get_argument('origin')
		destination = self.get_argument('destination')
		all_paths = nx.all_shortest_paths(graph_builder.graph,origin,destination)
		result = {}
		for path in all_paths:
			route=[]
			stops = " - ".join(path)
			for k,v in zip(path,path[1:]):
				edges = graph_builder.graph[k][v]
				legs = []
				for edge in edges.values():
					legs.append(edge['route'])
				route.append((k,v,legs))
			result[stops]=route
		self.content_type = 'application/json'
		self.write(json.dumps(result))

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", MainHandler)
		]
		settings = {
			"template_path": TEMPLATE_PATH,
			"static_path": STATIC_PATH,
		}
		tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
	graph_builder = GraphBuilder()
	application = Application()
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()