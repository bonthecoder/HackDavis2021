from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return jsonify(reallyintensebackendcode())

@app.route('/app')
def hello_world2():
    param1 = request.args.get('input1')
    return str(int(param1) * 12)



def reallyintensebackendcode():
    return [{"coolthing": 4, "notcoolthing": 3}]