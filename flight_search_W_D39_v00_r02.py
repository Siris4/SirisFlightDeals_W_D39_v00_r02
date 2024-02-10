# This class / tab is responsible for talking to the Flight Search API AKA http requests, endpoints, API_Keys, temporary 'TESTING' code.
import requests, os

# Constants:
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2"
TEQUILA_APP_ID = os.environ.get('TEQUILA_APP_ID', 'Custom Message / Key does not exist')
print(f"The TEQUILA_APP_ID is: {TEQUILA_APP_ID}")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API AKA http requests, endpoints, API_Keys, temporary 'TESTING' code.
