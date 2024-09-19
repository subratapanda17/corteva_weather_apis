from flask import Blueprint, jsonify, request
from flask_restx import Resource, Api, fields, Namespace
from api.modules.functions.get_weather_data import GET_WEATHER_DATA
from api.modules.schemas.get_weather_data import get_weather_data_model

# Create a blueprint for the weather data ingestion endpoint
get_weather_data_ns = Namespace('get_weather_data', description='Weather data insert')

@get_weather_data_ns.route('/getWeatherData/')
class GETWeatherData(Resource):
    @get_weather_data_ns.expect(get_weather_data_model)
    def get(self):
        req_obj = request.json
        response = GET_WEATHER_DATA(date,weather_station_id).fetch_weather_data(page_no)
        return response
