import web
import json
import cleAPI
import requests

key = cleAPI.API_key

urls = (
    '/([0-9]{5}),([A-Za-z]{2})', 'Weather',
    '/(.*)', 'error',
)
app = web.application(urls, globals())


class Weather:
    def GET(self, codePostal, countryCode):
        web.header('Content_Type', 'application/json')
        base_url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + codePostal + ',' + countryCode + '&appid=' + key
        data_weather = requests.get(base_url).json()
        temp_actuelle = data_weather.get('main').get('temp')
        temp_min = data_weather.get('main').get('temp_min')
        temp_max = data_weather.get('main').get('temp_max')
        meteo = data_weather.get('weather')[0].get('main')
        jsonResponse = json.dumps({
            'main': {
                'temp': self.k_to_c(temp_actuelle),
                'temp_max': self.k_to_c(temp_max),
                'temp_min' : self.k_to_c(temp_min),
                'meteo': meteo

            }
        })
        return jsonResponse

    # def getField(self, cle, valeur, dataJson):
    #     return dataJson.get('cle').get('valeur')

    def k_to_c(self, temperature):
        celsius = temperature - 273.15
        return celsius


if __name__ == "__main__":
    app.run()
