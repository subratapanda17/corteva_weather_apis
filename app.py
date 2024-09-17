from flask import Flask, jsonify, request, Blueprint
from flask_restplus import Api

# from app.connectors

app = Flask(__name__)
api = Api(app)

ns_conf = api.namespace(
    "Weather api resources",
    description = "Route for corveta coding challange weather data apis"
)