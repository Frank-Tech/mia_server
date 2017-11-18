from flask import Flask, Response

from queryHandler import QueryHandler
from fcmManager import fcmManager;

app = Flask(__name__)


# Connect to the database
# connection = pymysql.connect(host='52.14.253.14',
#                              user='root',
#                              password='Aa123456',
#                              db='mia',
#                              port=3306)

# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='miaSqlServer113',
#                              db='mia',
#                              port=3306)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user')
def insert_user():
    return Response(QueryHandler().new_user(), status=200)


@app.route('/location')
def update_location():
    return Response(QueryHandler().location_update(), status=200)


@app.route('/get_locations')
def get_locations():
    return Response(QueryHandler().locations_get(), status=200)


@app.route('/block')
def block():
    return Response(status=200)

@app.route('/push')
def push():
    return Response(fcmManager().send(), status=200);



if __name__ == '__main__':
    app.run(host="0.0.0.0")
