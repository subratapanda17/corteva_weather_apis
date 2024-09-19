import logging
from flask import Flask, jsonify
from flask_restx import Api, Namespace, Resource
from api.endpoints.weather_data_ingestion import weather_ingestion_ns
from api.endpoints.get_weather_data import get_weather_data_ns
from api.endpoints.get_weather_stats import get_weather_stats_ns

# Configure logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

# Initialize Flask-RESTX Api
api = Api(
    app,
    version="1.0",
    title="Weather API",
    description="An API for retrieving and processing weather data.",
    doc="/docs"  # Swagger UI available at /docs
)

# Define a basic error handler
@app.errorhandler(Exception)
def handle_exception(e):
    # Log the exception
    app.logger.error(f"An error occurred: {str(e)}")
    # Return a JSON response
    return jsonify({"error": str(e)}), 500

# Define a test namespace
test_ns = Namespace('test', description="Test Namespace")

@test_ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        app.logger.debug("In hello route")
        return {"message": "Hello, World!"}

# Register namespaces
api.add_namespace(test_ns, path='/api')
api.add_namespace(weather_ingestion_ns, path='/api')
api.add_namespace(get_weather_data_ns, path='/api')
api.add_namespace(get_weather_stats_ns, path='/api')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5001", debug=True)
