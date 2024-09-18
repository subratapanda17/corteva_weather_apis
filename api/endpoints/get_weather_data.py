from flask import Blueprint, jsonify
from flask_restx import Resource, Api, fields
from api.modules.schemas.get_weather_data import get_weather_data_model
from api.modules.functions.get_weather_data import GET_WEATHER_DATA

# Create a blueprint for the weather data ingestion endpoint
weather_get_bp = Blueprint('get_weather_data', __name__)
api = Api(weather_get_bp)

@api.route('/getWeatherData/')
class GETWeatherData(Resource):
    @api.expect(get_weather_data_model)
    def get(self):
        
        return jsonify("getweatherdata NONE")
