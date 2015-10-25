Airline-Scrapper
================

NOTE: This script is for demo purpose only.
      Programming Club or any person related to it shall not be held responsible for their misuse.

- Displays all the airline flights
- Displays all the airline codes
- Search all the flights for speciifc airline/country
- Displays 15 days history of specific flight
- Displays different timezones based on departure/arrival country
- Tabluate the output results

##USAGE

Using this script you can track/check/search flight details.

Airline scrapper

```
optional arguments:
  -h, --help            Show this help message and exit
  -lc                   Lists all the airline codes
  -s  SEARCH_CODES      Enter the airline/country name
  -af AIRLINE_FLIGHTS   Enter Airline code (Ex. AAL, AIC). Use -lc to display
                        airline codes or use -s to search
  -fh FLIGHT_HISTORY    Enter flight code
```

##Example
The below example displays the 15 days history for flight AIC102 in tabular form

`python airline.py -fh AIC102`

| Date          | From                                      | To                                         | Departure - Arrival        | Duration     |
| ------------- | ------------------------------------------|------------------------------------------- | ---------------------------| -------------|
| 12-Oct-2015   | Indira Gandhi Int'l (New Delhi IN) - VIDP |Chatrapati Shivaji Int'l (Mumbai IN) - VABB | 16:55 IST - 18:55 IST      | Scheduled    |
| 11-Oct-2015   | John F Kennedy Intl (New York, NY) - KJFK |Indira Gandhi Int'l (New Delhi IN) - VIDP   | 16:25 EDT - 15:02 IST (+1) | On The Way!  |
