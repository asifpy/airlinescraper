import argparse

from airlinescraper.results import Result

def main():
	parser = argparse.ArgumentParser(description='Airline scrapper')
	parser.add_argument('-lc',
		dest='airline_codes', 
		action="store_true",
		help="Lists all the airline codes",
		required=False,
		default=False
		)
	
	parser.add_argument('-s',
		dest='search_codes',
		help="Enter the airline/country name",
		required=False,
		default=False
		)

	parser.add_argument('-af',
		dest='airline_flights', 
		help='Enter Airline code (Ex. AAL, AIC). Use -lc to display airline codes or use -s to search', 
		required=False
		)

	parser.add_argument('-fh', 
		dest='flight_history',
		help='Enter flight code',
		required=False
		)

	args = parser.parse_args()

	for key, value in vars(args).items():
		if value:
			result = Result(value)
			print getattr(result, 'display_{}'.format(key))
			break

if __name__ == '__main__':
    main()
