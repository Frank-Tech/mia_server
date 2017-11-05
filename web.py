from flask import Flask
import pymysql
app = Flask(__name__)

# #Connect to the database
# connection = pymysql.connect(host='52.14.253.14',
#                              user='mia',
#                              password='h^*0uF^Q4bFSI2Xu',
#                              db='mia',
#                              port='3306')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
