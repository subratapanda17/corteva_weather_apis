from flask import Blueprint, jsonify
from flask_restx import Resource, Api, fields, Namespace
from api.modules.functions.weather_data_ingestion import INGEST_WEATHER_DATA
from api.modules.schemas.weather_data_ingestion import weatherIngetionParser
from api.config import settings
from flask import current_app as app

weather_ingestion_ns = Namespace(settings.COMMON_NAMESPACE_NAME, description=settings.COMMON_NAMESPACE_DESCRIPTION)

@weather_ingestion_ns.route('/weatherIngestion/')
class WeatherDataIngest(Resource):
    @weather_ingestion_ns.expect(weatherIngetionParser)
    @weather_ingestion_ns.doc(
        description="Ingest weather data into the MySQL Database",
        responses=settings.doc_responses
    )
    def get(self):
        app.logger.info("Received request for weather data insertion")
        try:
            response = INGEST_WEATHER_DATA().insert_weather_data()
            app.logger.info("Request complete")
            return response, getattr(settings, response.get("status"))
        except Exception as e:
            app.logger.error(f"Error during weather data ingestion: {str(e)}")
            return {"error": str(e)}, e.code