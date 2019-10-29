import requests
import datetime
from pytz import timezone


def main():
    url = 'https://www.bitmex.com/api/v1/trade/bucketed'
    params = {
            'binSize': '1d',
            'symbol': 'XBT',
            'startTime': datetime.datetime(2019, 10, 1),
            'endTime': datetime.datetime.now(timezone('UTC'))
            }

    response = requests.get(url, params=params)
    print(response)
    print(response.url)
    print(len(response.json()))
    for info in response.json():
        print(info['timestamp'])
        print(info['volume'])
        print('-------------------------------------')


if __name__ == "__main__":
    main()
