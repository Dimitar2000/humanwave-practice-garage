from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    response = jsonify(["Worker"])
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:8080')
    return response

if __name__ == "__main__":
    app.run(host="localhost", port=8082)