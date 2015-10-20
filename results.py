from airlinescraper.scraper import AirlineScraper

BASE_URL = "https://uk.flightaware.com/live/fleet/"
FLIGHT_HISTORY = "https://uk.flightaware.com/live/flight/"


class Result:
	"""Display results based on user input"""

	def __init__(self, input_value):
		self.input_value = input_value
		self.base_scrapper = AirlineScraper(BASE_URL, "prettyTable")

	@property
	def display_airline_codes(self):
		return self.base_scrapper.display_airline_codes()

	@property
	def display_search_codes(self):
		return self.base_scrapper.search_airline_code(self.input_value)

	@property
	def display_airline_flights(self):
		if self.base_scrapper.check_code_exist(self.input_value):
			url = '{}{}'.format(BASE_URL, self.input_value)
			new_scrapper = AirlineScraper(url, "prettyTable")
			return new_scrapper.display_airline_flights()
		else:
			return "Airline code doesn't exist"

	@property
	def display_flight_history(self):
		url = '{}{}'.format(FLIGHT_HISTORY, self.input_value)
		new_scrapper = AirlineScraper(url, "prettyTable")
		return new_scrapper.flight_history()