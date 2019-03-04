import requests
import datetime
import json
import secret


#Autorization step

URL = 'https://digital.iservices.rte-france.com/token/oauth/'
headers = {'Authorization' : 'Basic '+secret.token}

r = requests.post(URL, headers=headers)
print(r)

token = r.json()['access_token']


#API access

# sandbox URL='https://digital.iservices.rte- france.com/open_api/generation_forecast/v2/sandbox/forecasts'
rURL='https://digital.iservices.rte-france.com/open_api/generation_forecast/v2/forecasts'
headers = {'Authorization':'Bearer '+token}


#payload = {'start_date' : '2019-03-04T00:00:00Z' , 'end_date' : '2019-03-06T00:00:00Z' }

payload = {'type' : 'D-1' , 'production_type' : 'AGGREGATED_FRANCE,WIND,SOLAR' }


r = requests.get(rURL, params=payload, headers=headers)

p = json.dumps(r.json(),indent = 4)
print("===========print(p)")
print(p)
print("===========")

print()

print('--------------------------')
i = 0
for l in r.json()['forecasts']:
	print('Element ',i)
	print(l['start_date'])
	print(l['end_date'])
	print(l['production_type'])
	print('--------------------------')
	i+=1

for k,v in r.headers.items():
	print(k,":",v)

