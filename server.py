from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/sentiment', methods = ['POST'])
def get_sentiment():
    print request.json['inputVar']
    return jsonify({'data': 'Hello from server!!'})

@app.route('/')
def index():
    return render_template('main.html')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    app.run(debug = True)
