from flask import Flask
from flask_restx import Api, Namespace, Resource
# from api.endpoints.get_weather_data import weather_data_ns
# from api.endpoints.get_weather_stats import weather_stats_ns
from api.endpoints.weather_data_ingestion import weather_ingestion_ns

app = Flask(__name__)

# Initialize Flask-RESTX Api
api = Api(
    app,
    version="1.0",
    title="Weather API",
    description="An API for retrieving and processing weather data.",
    # doc="/docs"  # Swagger UI available at /docs
)


test_ns = Namespace('test', description="Test Namespace")

@test_ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}

api.add_namespace(test_ns, path='/api')

# Register namespaces   
# api.add_namespace(weather_data_ns, path='/weather')
# api.add_namespace(weather_stats_ns, path='/weather/stats')
api.add_namespace(weather_ingestion_ns, path='/api/')

if __name__ == "__main__":
    app.run(debug=True)
