from flask import Blueprint, jsonify, request
from flask_restx import Resource, Api, fields, Namespace
from api.modules.functions.get_weather_data import GET_WEATHER_DATA
from api.modules.schemas.get_weather_data import getWeatherDataParser

get_weather_data_ns = Namespace('get_weather_data', description='Weather data fetch')

@get_weather_data_ns.route('/getWeatherData/')
class GETWeatherData(Resource):
    @get_weather_data_ns.expect(getWeatherDataParser)
    def get(self):
        req_obj = getWeatherDataParser.parse_args(strict=True)
        date = req_obj.get('date')
        weather_station_id = req_obj.get('weather_station_id')
        page_no = req_obj.get('page_no')

        response = GET_WEATHER_DATA(date, weather_station_id).fetch_weather_data(page_no)
        return response
