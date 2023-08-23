
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!"


@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    result = data["first"]+data["second"]
    response = {"result": result}
    return jsonify(response), 200


@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    result = data["first"]-data["second"]
    response = {"result": result}
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')