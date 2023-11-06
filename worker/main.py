from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    print("Called")
    response = jsonify(["Worker"])
    return response

if __name__ == "__main__":
    app.run(host="localhost", port=8082)