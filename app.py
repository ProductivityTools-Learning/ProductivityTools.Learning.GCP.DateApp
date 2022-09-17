from flask import Flask
from flask_restful import Api
from DateResource import DateResource

def create_app():
    app=Flask(__name__)
    api=Api(app)
    api.add_resource(DateResource,'/')