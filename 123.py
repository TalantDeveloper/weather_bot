import requests
import need

url = 'https://api.weatherapi.com/v1/current.json?key=93e7b2612c5d436897652816243006&q='

for city in need.region:
    data = requests.get(url+city['name']).json()
    # print(data['location'])
    # print(data['current'])
    # print(data['current']['temp_c'])
    content = {
        'joylashuv': f"{data['location']['name']}, {data['location']['country']}.",
        'vaqt': data['location']['localtime'],
        'temp': data['current']['temp_c'],
        'holat': data['current']['condition']['text'],
        'icon': data['current']['condition']['icon'][2:]
    }
    print(content)
