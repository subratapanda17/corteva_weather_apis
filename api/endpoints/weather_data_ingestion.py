from flask import Blueprint, jsonify
from flask_restx import Resource, Api, fields, Namespace
from api.modules.functions.weather_data_ingestion import INGEST_WEATHER_DATA
from api.modules.schemas.weather_data_ingestion import weatherIngetionParser

weather_ingestion_ns = Namespace('weather_data_ingestion', description='Weather data insert')

@weather_ingestion_ns.route('/weatherIngestion/')
class WeatherDataIngest(Resource):
    @weather_ingestion_ns.expect(weatherIngetionParser)
    def get(self):

        response = INGEST_WEATHER_DATA().insert_weather_data()
        return response