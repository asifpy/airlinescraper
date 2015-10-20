import requests
from tabulate import tabulate
from bs4 import BeautifulSoup


class AirlineScraper:
	
	def __init__(self, baseurl, class_name):
		self.baseurl = baseurl
		self.class_name = class_name
		page = requests.get(self.baseurl).text
		self.soup = BeautifulSoup(page, "lxml")
		self.table = self.soup("table", class_ = self.class_name)

	def prepare_airline_codes(self):
		codes = []
		for row in self.table[0].findAll('tr')[2:]:
			col = row.findAll('td')
			no_of_flights = col[0].string
			airline_code = col[1].string
			airline_name = col[2].string
			codes.append([no_of_flights, airline_code, airline_name])
		return codes

	def display_airline_codes(self):
		codes = self.prepare_airline_codes()
		return tabulate(codes, headers=['# of flights', 'Code', 'Airline'], tablefmt='orgtbl')

	def search_airline_code(self, search_key):
		codes = self.prepare_airline_codes()
		search_key = search_key.lower()
		result = filter(lambda x: search_key in x[1].lower() or search_key in x[2].lower(), codes)
		return tabulate(result, headers=['# of flights', 'Code', 'Airline'], tablefmt='orgtbl')

	def check_code_exist(self, airline_code):
		codes = self.prepare_airline_codes()
		return filter(lambda x: airline_code == x[1], codes)

	def get_flight_to_from_time(self, col):
		flight_from = col[2].find('span')['title']
		flight_to = col[3].find('span')['title']
		departure = col[4].text.encode('utf-8')
		arrival = col[5].text.encode('utf-8')
		time = '{} - {}'.format(departure, arrival).decode('utf-8')
		return {
			'flight_from' : flight_from,
			'flight_to'   : flight_to,
			'time'   	  : time
			}

	def display_airline_flights(self):
		flights = []
		for row in self.table[0].findAll('tr')[2:]:
			col = row.findAll('td')
			flight_id = col[0].find('a').text
			details = self.get_flight_to_from_time(col)
			flights.append([flight_id, details['flight_from'], details['flight_to'], details['time']])

		headers = ['Flight No.', 'From', 'To', 'Departure - Arrival']
		return tabulate(flights, headers=headers, tablefmt='orgtbl')

	def flight_history(self):
		history = []
		if not self.table:
			return "Flight doesn't exist for the entered flight number"

		for row in self.table[0].findAll('tr')[2:]:
			col = row.findAll('td')
			if not col[0].get('colspan'):
				date = col[0].find('a').text
				details = self.get_flight_to_from_time(col)
				duration = col[6].text
				history.append([date, details['flight_from'], details['flight_to'], details['time'], duration])

		headers = ['Date', 'From', 'To', 'Departure - Arrival', 'Duration']
		return tabulate(history, headers=headers, tablefmt='orgtbl')
