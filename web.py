from flask import Flask
import pymysql
app = Flask(__name__)

#Connect to the database
# connection = pymysql.connect(host='52.14.253.14',
#                              user='root',
#                              password='Aa123456',
#                              db='mia',
#                              port=3306)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='miaSqlServer113',
                             db='mia',
                             port=3306)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
