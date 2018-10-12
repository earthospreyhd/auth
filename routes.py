from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import request
from signup import signup
from login import login
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
        response_data = signup(args)
        return response_data

class api_login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_hash")
        parser = add_argument("pin")
        parser = add_argument("user_secret")
        parser = add_argument("email")
        parser = add_argument("devid")
        args = parser.parse_args()
        login_success = login(args["user_secret"], args["pin"], args["user_hash"], args["email"], args["devid"])

        return login_success

# class email(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument("email")
#         args = parser.parse_args()
#         email = args["email"]
#         email.send_email("some content", email)

api.add_resource(api_signup, "/api_signup")

if __name__ == "__main__":
    app.run(debug=True)