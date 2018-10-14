from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import request
from signup import signup
from login import login
from increment import increment
import authlib
import email
import db_query
import json

app = Flask(__name__)
api = Api(app)

class api_signup(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("code")
        args = parser.parse_args()
        cookie = signup(args)

        if success = True:
            response_data = {
                "status": "success",
                ""
            }
        return response_data

class api_login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_hash")
        parser = add_argument("pin")
        parser = add_argument("user_secret")
        parser = add_argument("email")
        parser = add_argument("devid")
        parser = add_argument("nonce")
        args = parser.parse_args()

        login_success = login(
            args["user_secret"],
            args["pin"],
            args["user_hash"],
            args["email"],
            args["devid"],
            args["nonce"]
            )

        if login_success == True:
            half_increment = increment(user_nonce, args["email"], args["devid"])
            response = {
                "status": "success",
                "increment": half_increment,
            }

        else:
            response = {
                "status": "failure",
                "error": "invalid crediantials, try again"
            }

        return response

api.add_resource(api_signup, "/api_signup")
api.add_resource(api_login, "/api_login")

if __name__ == "__main__":
    app.run(debug=True)