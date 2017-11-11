from flask import Flask, Response

from queryHandler import QueryHandler

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
    new_user = QueryHandler().new_user()
    response = Response(new_user, status=200)
    return response

@app.route('/location')
def update_location():
    location = QueryHandler().location_update()
    response = Response(location, status=200)
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0")
