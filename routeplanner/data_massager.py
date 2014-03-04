import json

def make_routes_dict(routes):
	routes_dict ={route['name']:route for route in routes}
	return routes_dict

def get_from_json(file):
	return json.loads(open(file).read())

def main():
	f = open('routes.json','w')
	routes = get_from_json('../busroutes/hyd_routes.json')
	routes_dict = make_routes_dict(routes)
	route_info = get_from_json('../busroutes/hyd_routes_info.json')
	for info in route_info:
		route = routes_dict[info['name']]
		route['stops'] = info['stops']
	json.dump(routes_dict.values(),f,indent=4)	
	f.close()

if __name__ == "__main__":
	main()