from flask import Flask
from flask_restful import Resource, Api, reqparse
# import pandas as pd
# import ast

from .endpoints import init


def create_api():
    app = Flask(__name__)
    api = Api(app)

    init(api)

    return app
