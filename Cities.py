import requests

API_KEY = "0904ac61a03b113c793d2290ea492308"
URL = "https://api.openweathermap.org/data/2.5/forecast"


class City(object):

	def __init__(self, city_id):

		query = '?id={}&apikey={}&&units=imperial'.format(city_id, API_KEY)
		response = requests.get(URL + query)
		if 200 == response.status_code:
			d = response.json()
			self.all_temps = [d['list'][i]['main']['temp_max'] for i in range(40)]
			self.name = d['city']['name']
			self.day_temp = [-999, -999, -999, -999, -999]

			for day in range(5):
				for j in range(8):
					if self.all_temps[8 * day + j] > self.day_temp[day]:
						self.day_temp[day] = self.all_temps[8 * day + j]
		else:
			print('something went wrong')