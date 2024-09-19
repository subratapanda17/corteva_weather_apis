import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask, jsonify
from flask_restx import Api, Namespace, Resource


# Logging configuration for the apps running
def configure_logging(app):
    log_file = 'api/logs/app.log'
    file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=2, backupCount=3)  #  refresh log at midnight every 2 days, keeping last 3 days backup
    file_handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.DEBUG)


# App configuration
def create_app():
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
    
    # adding default error handler
    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500
    

    # adding the api blueprints
    api.add_namespace(weather_ingestion_ns, path='/api')
    api.add_namespace(get_weather_data_ns, path='/api')
    api.add_namespace(get_weather_stats_ns, path='/api')

    # addinng the logger
    configure_logging(app)

    return app


# main function
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0",port="5000", debug=True)
