import requests
import json
import pprint

# Authorization step
URL = 'https://digital.iservices.rte-france.com/token/oauth/'
headers = {'Authorization': 'Basic YWY1NmZiYzctZTc1OS00NDMwLTkzYzMtYjk5NTRlYTgxYmNiOjJjNTliZTMx'
                            'LWU2MWMtNDdjMS1iZmI1LWM4YTU1ZGRlZDhiYw=='}  # TODO store the secret elsewhere
r = requests.post(URL, headers=headers)
print(r)
token = r.json()['access_token']  # store the requested token

# API access
'''
sandbox URL='https://digital.iservices.rte-france.com/open_api/generation_forecast/v2/sandbox/forecasts'
If needed this code display the response header :
for k,v in r.headers.items():
	print(k,":",v)
'''

rURL = 'https://digital.iservices.rte-france.com/open_api/generation_forecast/v2/forecasts'
headers = {'Authorization': 'Bearer ' + token}
# Get data for tomorrow only for these 3 production type
payload = {'type': 'D-1', 'production_type': 'AGGREGATED_FRANCE,WIND,SOLAR'}

# Other payload parameters if needed
# payload = {'start_date' : '2019-03-04T00:00:00Z' , 'end_date' : '2019-03-06T00:00:00Z' }

r = requests.get(rURL, params=payload, headers=headers)

# Displaying the response in a readable format
# p = json.dumps(r.json(), indent=4)
# print("===========")
# print(p)
# print("===========")

# Storing the forecasts list in a variable called "forecasts". Each element of the list is a dictionary
forecasts = r.json()['forecasts']
print(len(forecasts))

print('--------------------------')  # printing the structure of the different dictionaries
for f in forecasts:
	print('Element ', forecasts.index(f))
	print(f.keys())
	print(f['start_date'])
	print(f['end_date'])
	print(f['type'])
	print(f['production_type'])
	print('--------------------------')

# Storing each production_type forecasts in a specific variable. Each variable is a list of dictionaries
for f in forecasts:
	if f["production_type"] == "SOLAR":
		SOLAR_forecast = f["values"]
	if f["production_type"] == "WIND":
		WIND_forecast = f["values"]
	if f["production_type"] == "AGGREGATED_PROGRAMMABLE_FRANCE":
		PROGRAMMABLE_FRANCE_forecast = f["values"]
	if f["production_type"] == "AGGREGATED_NON_PROGRAMMABLE_FRANCE":
		NON_PROGRAMMABLE_FRANCE_forecast = f["values"]

table = [["start", "end", "SOLARupdate", "SOLARvalue", "WINDupdate", "WINDvalue"]]
for f in SOLAR_forecast:
	table.append([f["start_date"], f["end_date"], f["updated_date"], f["value"]])

pprint.pprint(WIND_forecast)
for row in table:
	for f in WIND_forecast:
		if row[0] == f["start_date"]:
			row.append(f["updated_date"])
			row.append(f["value"])

#pprint.pprint(table)
print(json.dumps(table, indent=2))

#	print(type(f))

# pprint.pprint(table)


