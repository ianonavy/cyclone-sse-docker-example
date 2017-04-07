import datetime
import redis
from flask import Flask, render_template

import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/push')
def push():
    with pymysql.connect(host='db', user='root', password='root') as cur:
        cur.execute('select current_timestamp()')
        data = cur.fetchall()[0][0]

    redis_conn = redis.Redis('redis')
    redis_conn.publish('channel', data)
    return 'OK'


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
