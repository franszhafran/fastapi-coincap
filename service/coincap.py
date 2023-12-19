import requests

class CoincapService():
    def assets(self):
        url = "https://api.coincap.io/v2/assets"

        response = requests.request("GET", url)

        return response.json()['data']

    def get_price(self, coin: str):
        url = "https://api.coincap.io/v2/assets/{}".format(coin)
        response = requests.request("GET", url)
        return float(response.json()['data']['priceUsd'])
        
    def get_usd_rate(self):
        url = "https://openexchangerates.org/api/latest.json?app_id=0026060aa84640baac6379be39269326"
        response = requests.request("GET", url)
        return float(response.json()['rates']['IDR'])