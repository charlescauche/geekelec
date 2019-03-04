import requests
import datetime
import json
import secret



# base = "YWY1NmZiYzctZTc1OS00NDMwLTkzYzMtYjk5NTRlYTgxYmNiOjJjNTliZTMxLWU2MWMtNDdjMS1iZmI1LWM4YTU1ZGRlZDhiYw=="

#Autorization step

URL = 'https://digital.iservices.rte-france.com/token/oauth/'
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization' : 'Basic '+secret.token}

r = requests.post(URL, headers=headers)

print(r)

token = r.json()['access_token']


#API access

#sbURL='https://digital.iservices.rte- france.com/open_api/generation_forecast/v2/sandbox/forecasts'
rURL='https://digital.iservices.rte-france.com/open_api/generation_forecast/v2/forecasts'
headers = {'Authorization':'Bearer '+token}

# print('=====================')
# print(datetime.date.today())
# print('=====================')

payload = {'start_date' : '2019-03-04T00:00:00Z' , 'end_date' : '2019-03-06T00:00:00Z' }


r = requests.get(rURL, params=payload, headers=headers)

print("===========")
p = json.dumps(r.json(),indent = 4)
print(p)

