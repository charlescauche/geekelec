import requests
import datetime


# user = "af56fbc7-e759-4430-93c3-b9954ea81bcb"
# pwd = "2c59be31-e61c-47c1-bfb5-c8a55dded8bc" 
# base = "YWY1NmZiYzctZTc1OS00NDMwLTkzYzMtYjk5NTRlYTgxYmNiOjJjNTliZTMxLWU2MWMtNDdjMS1iZmI1LWM4YTU1ZGRlZDhiYw=="

#Autorization step

URL = 'https://digital.iservices.rte-france.com/token/oauth/'
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization' : 'Basic YWY1NmZiYzctZTc1OS00NDMwLTkzYzMtYjk5NTRlYTgxYmNiOjJjNTliZTMxLWU2MWMtNDdjMS1iZmI1LWM4YTU1ZGRlZDhiYw=='}

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

print(r.json())
print(r)