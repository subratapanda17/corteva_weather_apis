from flask import Blueprint, jsonify
from flask_restx import Resource, Api, fields, Namespace
from api.modules.functions.weather_data_ingestion import InsertWeatherData
from api.modules.schemas.weather_data_ingestion import weather_data_ingestion_model


weather_ingestion_ns = Namespace('weather_data_ingestion', description='Weather data insert')


@weather_ingestion_ns.route('/weather_ingestion')
class WeatherDataIngest(Resource):
    @weather_ingestion_ns.expect(weather_data_ingestion_model)
    def get(self):
        return jsonify("into weather ingestion")
        result = InsertWeatherData().insert_weather_data()
        
        return jsonify(result)