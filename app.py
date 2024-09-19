import logging
from flask import Flask, jsonify
from flask_restx import Api, Namespace, Resource


def configure_logging(app):
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)


def create_app():
    #Cofigure app
    from api.endpoints.weather_data_ingestion import weather_ingestion_ns
    from api.endpoints.get_weather_data import get_weather_data_ns
    from api.endpoints.get_weather_stats import get_weather_stats_ns

    app = Flask(__name__)
    api = Api(
        app,
        version="v1.1",
        title="CORVETA Weather API",
        description="An API for saving, retrieving and processing weather data.",
        doc="/docs"  
    )
    
    #Adding default error handler
    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500
    

    api.add_namespace(weather_ingestion_ns, path='/api')
    api.add_namespace(get_weather_data_ns, path='/api')
    api.add_namespace(get_weather_stats_ns, path='/api')

    # Configure logging
    configure_logging(app)

    return app


#main function
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0",port="5000", debug=True)
