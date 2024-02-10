#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
from SirisFlightDeals_Sheety_JSON_Data_in_Py_Format import sheet_data

# TODO: Authenticate with a Bearer Token
# TODO: Ensure all sensitive data is extracted and created into an Environment Variable, above here.

print("The sheet data is \n")
pprint(sheet_data)   #pretty prints

# attempt #1:
# def checks_iata_codes():
#     valid_cities_with_iataCodes = []
#     for entry in sheet_data['prices']:
#         # temporarily change the iataCode to the string "TESTING", in the meantime
#         entry['iataCode'] = "TESTING"
#
#         if 'iataCode' in entry and entry['iataCode']:  # if there is an entry in the iataCode Value field..
#             print(f"(Temp) iataCode for {entry['city']}: {entry['iataCode']}")
#             print(f"{entry['city']} was added to the list of valid cities with iataCodes.")
#             valid_cities_with_iataCodes.append(entry['city'])      # NOT this option. It will break out of the block early -> return entry['city']
#         else:
#             print(f"iataCode for {entry['city']}: No iataCode found")
#     return valid_cities_with_iataCodes  # NOW you return the full list, at the very end of processing.
#
# valid_cities_with_iataCodes = checks_iata_codes()
# print("Cities with valid iataCodes: ", valid_cities_with_iataCodes)   # after the TESTING phase update

# attempt 2:

from pprint import pprint
# Ensure this path is correct and the module contains a properly defined sheet_data variable
from SirisFlightDeals_Sheety_JSON_Data_in_Py_Format import sheet_data

def checks_iata_codes():
    if sheet_data is None:
        print("sheet_data is not properly loaded ")
        return []
    if 'prices' not in sheet_data:
        print(f'prices key is missing.')
        return []

    valid_cities_with_iataCodes = []
    for entry in sheet_data['prices']:
        # Temporarily change the iataCode to the string "TESTING"
        entry['iataCode'] = "TESTING"

        print(f"(Temp) iataCode for {entry['city']}: {entry['iataCode']}")
        print(f"{entry['city']} was added to the list of valid cities with iataCodes.")
        valid_cities_with_iataCodes.append(entry['city'])

    return valid_cities_with_iataCodes

valid_cities_with_iataCodes = checks_iata_codes()
print("Cities with valid iataCodes:", valid_cities_with_iataCodes)

