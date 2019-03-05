import requests
import datetime
import json

import secret


### Autorization step
URL = 'https://digital.iservices.rte-france.com/token/oauth/'
headers = {'Authorization' : 'Basic '+secret.token}

r = requests.post(URL, headers=headers)
print(r)

token = r.json()['access_token'] #store the requested token


### API access
'''
sandbox URL='https://digital.iservices.rte- france.com/open_api/generation_forecast/v2/sandbox/forecasts'
If needed this code display the response header :
for k,v in r.headers.items():
	print(k,":",v)
'''

rURL='https://digital.iservices.rte-france.com/open_api/generation_forecast/v2/forecasts'
headers = {'Authorization':'Bearer '+token}
payload = {'type' : 'D-1' , 'production_type' : 'AGGREGATED_FRANCE,WIND,SOLAR' } # Get data for tomorrow only for these 3 porduction type

## Other payload parameters if needed
#payload = {'start_date' : '2019-03-04T00:00:00Z' , 'end_date' : '2019-03-06T00:00:00Z' }

r = requests.get(rURL, params=payload, headers=headers)

p = json.dumps(r.json(),indent = 4) #Displaying the response in a readable format
print("===========")
print(p)
print("===========")

forcasts = r.json()['forecasts'] # Storing the forcasts list in a variable called "forcasts". Each element of the list is a dictionary
print(len(forcasts))

print('--------------------------') #printing the structure of the different dictionaries
i = 0
for l in forcasts:
	print('Element ',i)
	print(l.keys())
	print(l['start_date'])
	print(l['end_date'])
	print(l['type'])
	print(l['production_type'])
	print('--------------------------')
	i+=1



#Storing each production_type forcasts in a specific variable. Each variable is a list of dictionaries
for e in forcasts:
	if e["production_type"] == "SOLAR":
		SOLAR_forcast = e["values"]
	if e["production_type"] == "WIND":
		WIND_forcast = e["values"]
	if e["production_type"] == "AGGREGATED_PROGRAMMABLE_FRANCE":
		PROGRAMMABLE_FRANCE_forcast = e["values"]
	if e["production_type"] == "AGGREGATED_NON_PROGRAMMABLE_FRANCE":
		NON_PROGRAMMABLE_FRANCE_forcast = e["values"]	


for i in WIND_forcast :
	print(i)

print(WIND_forcast[0].keys())



