from flask import Flask
import pymysql
app = Flask(__name__)

# #Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='mia',
#                              password='passwd',
#                              db='mia')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
