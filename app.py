import web
import json
# import cleAPI
import requests
import dotenv
import os
import pymysql.cursors

dotenv.load_dotenv()
API_Key = os.environ.get('API_KEY')
DB_Host = os.environ.get('DB_HOST')
DB_User = os.environ.get('DB_USER')
DB_Password = os.environ.get('DB_PASSWORD')
DB_Name = os.environ.get('DB_NAME')
DB_Port = os.environ.get('DB_PORT')

# connexion = pymysql.connect(
#     host=DB_Host,
#     user=DB_User,
#     password=DB_Password,
#     db=DB_Name,
#     charset='utf8',
#     port=int(DB_Port)
# )

# key = cleAPI.API_key

urls = (
    '/([0-9]{5}),([A-Za-z]{2})', 'Weather',
    '/(.*)', 'error',
)
app = web.application(urls, globals())


class Weather:
    def GET(self, codePostal, countryCode):
        web.headers = {"Content_Type": "application/json"}
        base_url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + codePostal + ',' + countryCode + '&appid=' + API_Key
        data_weather = requests.get(base_url).json()
        temp_actuelle = data_weather.get('main').get('temp')
        temp_min = data_weather.get('main').get('temp_min')
        temp_max = data_weather.get('main').get('temp_max')
        meteo = data_weather.get('weather')[0].get('main')
        humidite = data_weather.get('main').get('grnd_level')
        ville = data_weather.get('name')
        jsonResponse = json.dumps({
            'main': {
                'name': ville,
                'temp': self.k_to_c(temp_actuelle),
                'temp_max': self.k_to_c(temp_max),
                'temp_min': self.k_to_c(temp_min),
                'meteo': meteo,
                'humidité': humidite

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
