import web
import json
import requests
import dotenv
import os
import pymysql.cursors
import datetime

dotenv.load_dotenv()
API_Key = os.environ.get('API_KEY')
API_Adress = os.environ.get('API_ADRESS')

connexion = pymysql.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    db=os.environ.get('DB_NAME'),
    charset='utf8',
    port=int(os.environ.get('DB_PORT'))
)

# key = cleAPI.API_key

urls = (
    '/([0-9]{5}),([A-Za-z]{2})', 'Weather',
    '/(.*)', 'error',
)
app = web.application(urls, globals())


class Weather:
    def GET(self, codePostal, countryCode):
        web.header('Content_Type', 'application/json')
        web.header('charset', 'utf-8')
        # date_actuelle = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        base_url = API_Adress + codePostal + ',' + countryCode + '&appid=' + API_Key
        data_weather = requests.get(base_url).json()
        jsonResponse = json.dumps({
            'main': {
                'name': data_weather.get('name'),
                'temp': self.k_to_c(data_weather.get('main').get('temp')),
                'temp_max': self.k_to_c(data_weather.get('main').get('temp_max')),
                'temp_min': self.k_to_c(data_weather.get('main').get('temp_min')),
                'meteo': data_weather.get('weather')[0].get('main'),
                'humidité': data_weather.get('main').get('grnd_level')

            }
        }, indent=4)
        return jsonResponse

    # def getField(self, cle, valeur, dataJson):
    #     return dataJson.get('cle').get('valeur')

    def k_to_c(self, temperature):
        celsius = temperature - 273.15
        return celsius


if __name__ == "__main__":
    app.run()
