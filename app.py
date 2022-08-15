from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/convert/<string:typeFrom>/<string:typeTo>/<string:value>", methods=['GET'])
def convert(typeFrom, typeTo, value):
  response = jsonify(
    {
      "from": typeFrom,
      "to": typeTo,
      "value": value
    }
  )
  response.headers.add("Access-Control-Allow-Origin", "*")

  return response

app.run(host="192.168.43.239", port=5000, debug=True)