import datetime
import pymysql
import redis
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


def update_clients_with_current_db_time():
    with pymysql.connect(host='db', user='root', password='root') as cursor:
        cursor.execute('select current_timestamp()')
        (data,) = cursor.fetchone()

    redis_conn = redis.Redis('redis')
    redis_conn.publish('channel', data)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/push', methods=["POST"])
def push():
    if request.method == 'POST':
        update_clients_with_current_db_time()
    return redirect(url_for('index'))


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
