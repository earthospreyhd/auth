from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import request
from signup import signup
import authlib
import email
import db_query

app = Flask(__name__)
api = Api(app)

class api_signup(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("code")
        args = parser.parse_args()
        signup(args)
        return {"code": code}

class email(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email")
        args = parser.parse_args()

api.add_resource(api_signup, "/api_signup")

if __name__ == "__main__":
    app.run(debug=True)