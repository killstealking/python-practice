import requests

url = 'https://www.bitmex.com/api/v1/instrument'
params = {
        'symbol': 'XBTUSD',
        'startTime': "2019-10-13T12:00:00.000Z"
        }
response = requests.get(url, params=params)
print(response)
print(response.text)
