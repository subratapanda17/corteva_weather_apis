from flask import Flask
from flask_restx import Api
from api.endpoints.weather_data_ingestion import weather_bp

# Create the Flask app
app = Flask(__name__)

# Initialize Flask-RESTX API
api = Api(app)

# Register the blueprint
app.register_blueprint(weather_bp)

@app.route('/')
def home():
    return "API is running!"

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
