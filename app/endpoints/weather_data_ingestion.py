from flask_restplus import Resource
from app.restplus import api, ns_conf


ns_conf.route('/weather_data_ingestion/')
class WeatherDataInngestion:
    def get(self):
        return True

