from flask import Flask
from flask_restful import Api
from DateResource import DateResource
import os

def create_app():
    app=Flask(__name__)
    api=Api(app)
    api.add_resource(DateResource,'/')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)