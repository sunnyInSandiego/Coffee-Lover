from Cities import City
from route import Route

from itertools import permutations

temp = 0

cities = [City(5313667), City(5294810), City(5318313), City(5308655), City(5301388)]

routes = Route(cities).create_permutations()

routeTemps = []
minTempRoute = None
minTemp = 500
for route in routes:
	# Calculate average temp
	temp = 0
	for day, city in enumerate(route):
		temp = temp + city.day_temp[day] / 5.0
	routeTemps.append(temp)
	# Pick off route with minimum average temp
	if temp < minTemp:
		minTemp = temp
		minTempRoute = route

print("The lowest average temperature high {} is forecast for this route:".format(temp))

for day, city in enumerate(minTempRoute):
	print(city.name + ":" + " " + str(city.day_temp[day]))