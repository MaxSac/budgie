from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/data', methods=['POST'])
def data():

    data = request.get_json()
    temp = data["temp"]
    humi = data["humi"]
    poll = data["poll"]

    return f"successfull"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
