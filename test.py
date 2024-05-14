from flask import Flask, request, jsonify

app = Flask(__name__)

#  GET  = Eg. Seding data to a google server -> www.google.com(sending data through URL)

# POST = Eg. Gmail Login, ->(Sending data through Body(hidden))


@app.route("/xyz", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        a = request.json["num1"]
        b = request.json["num2"]
        result = a + b
        return jsonify(str(result))


@app.route("/abc/parth", methods=["POST"])
def test1():
    if request.method == "POST":
        a = request.json["num3"]
        b = request.json["num4"]
        result = a * b
        return jsonify(str(result))


if __name__ == "__main__":
    app.run()
