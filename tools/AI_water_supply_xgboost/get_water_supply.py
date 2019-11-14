import requests, json
from datetime import datetime

hour = int(datetime.now().strftime('%-H'))
temperature = float(requests.get('http://192.168.2.117:5000/temperature').text)

water_supply = requests.post(
'http://www.watarunrun.com:5000/preds',
json.dumps({"hour": hour, "temperature": temperature}),
headers={'Content-Type': 'application/json'}).text
print('Hour: ' + str(hour))
print('Temperature: ' + str(temperature))
print('Required water: ' +str(water_supply))
