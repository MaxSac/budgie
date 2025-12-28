from flask import Flask, request, g
from datetime import datetime 
import psycopg

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        # g.db = psycopg.connect(
        #         "dbname='testdb' user='testusr' password='testpwd' host='0.0.0.0'"
        # )

        g.db = psycopg.connect(
                dbname='testdb',
                user='testusr', 
                password='testpwd',
                host="192.168.178.37"
        )
    return g.db

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/data', methods=['POST'])
def data():

    data = request.get_json()
    temp = data["temp"]
    humi = data["humi"]
    poll = data["poll"]
    ts = f"{datetime.now()}"
    
    get_db().execute(
        t"INSERT INTO weather (ts, temp, humi, CO2) VALUES ({ts}, {temp}, {humi}, {poll})"
    )

    get_db().commit()

    return f"successfull"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
