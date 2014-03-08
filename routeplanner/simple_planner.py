import json
import networkx as nx
from itertools import izip

graph = nx.MultiGraph()

data_str = open('routes.json').read()
data = json.loads(data_str)

for item in data:
	route_name = item['name']
	stops = item['stops']
	stop_names = [stop['stop']['name'] for stop in stops]
	if stop_names!=[]:
		#graph.add_star(stop_names,route=route_name)
		graph.add_path(stop_names,route=route_name)
		#stop_names.reverse()
		#graph.add_path(stop_names,route=route_name)
		#graph.add_star(stop_names,route=route_name)

#print nx.shortest_path(graph,'Dilsukhnagar Bus station','Patancheru Bus Stop')
#print nx.shortest_path(graph,'Patancheru Bus Stop','Hayath Nagar Bus Stop')
#for path in nx.all_shortest_paths(graph,'Dilsukhnagar Bus station','Patancheru Bus Stop'):
#	print path
	
#all_paths =  nx.all_pairs_shortest_path(graph)
#path = all_paths['Chaitanyapuri']['Ziaguda']
paths = nx.all_shortest_paths(graph,'Chaitanyapuri','Ziaguda')
for path in paths:
	for k,v in zip(path,path[1:]):
		edges = graph[k][v]
		routes = []
		for edge in edges.values():
			routes.append(edge['route'])
		#print k,v,routes
	print path