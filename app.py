import web
import json
import cleAPI
import requests

key = cleAPI.API_key
# client = zeep.Client(base_url)
# client.service

urls = (
    '/([0-9]{5})', 'Weather',
    '/(.*)', 'error',
)
app = web.application(urls, globals())


class Weather:
    def GET(self, codePostal):
        base_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + codePostal + '&appid=' + key
        data_weather = requests.get(base_url).json()
        return data_weather


if __name__ == "__main__":
    app.run()
