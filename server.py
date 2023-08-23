
from flask import Flask, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world'


@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    added = data.first + data.second
    return added


@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    Nadded = data.first - data.second
    return Nadded


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')