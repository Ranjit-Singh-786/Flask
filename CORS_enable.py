from flask import Flask, jsonify ,request
from flask_cors import CORS
app  = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.after_request
def apply_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, DELETE, PUT"
    response.headers["Access-Control-Max-Age"] = "3600"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Accept, SagAuthToken, Access-Control-Allow-Headers, X-Requested-With, remember-me, Authorization"
    return response

@app.route("/home")
def home():
    return jsonify({'status':200,'message':'successfully enabled'})


if __name__ == "__main__":
    app.run()