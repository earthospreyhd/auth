from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import request
from signup import signup
from login import login
from increment import increment
import email
import db_query
import json
from send_code import send_code
from authlib import gen_code
from custom_errors import EmailError, CodeError, DataBaseError

app = Flask(__name__)
api = Api(app)

class api_get_code(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email")
        parser.add_argument("pin")
        parser.add_argument("devid")
        args = parser.parse_args()
        
        try:
            send_code(args["email"], args["pin"], args["devid"])
            response = {
                "status": "success"
            }
        except EmailError as err:
            response = {
                "status": "failed to send email",
                "error": err.args[0]
            }
        
        return response

class api_signup(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("code")
        parser.add_argument("email")
        parser.add_argument("pin")
        parser.add_argument("devid")
        parser.add_argument("user_secret")
        args = parser.parse_args()

        try:
            cookie = signup(args["email"], args["pin"], args["devid"], args["code"], args["user_secret"])

            response_data = {
                "status": "success",
                "user_hash": cookie
            }
        except (DataBaseError, CodeError) as err:
            response_data = {
                "status": "failure",
                "error": err.args[0]
            }

        
        return response_data

class api_login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_hash")
        parser.add_argument("pin")
        parser.add_argument("user_secret")
        parser.add_argument("email")
        parser.add_argument("devid")
        parser.add_argument("nonce")
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
            half_increment = increment(args["nonce"], args["email"], args["devid"])
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
api.add_resource(api_get_code, "/api_get_code")

if __name__ == "__main__":
    app.run(debug=True)