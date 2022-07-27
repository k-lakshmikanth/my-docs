from flask import request
import flask
import pymssql
import pandas as pd

app = flask.Flask(__name__)

@app.route('/')
def home():
    return "<h1>RELATIVE URL = /DATABASE_NAME/TABLE_NAME?key=AUTH_KEY</h1>"


@app.route('/<str1>/<str2>')
def hello(str1,str2):
    key=request.args.get("key")
    if key == "lkjuly$2022":
        conn = pymssql.connect(host="sqldev002.database.windows.net",port=1433,database=str1,user='sqladmin@sqldev002',password='lkjuly$2022')
        df = pd.read_sql("SELECT * FROM "+str2,conn)
        return df.to_json()
    else:
        return "AUTHENTICATION FAILURE"
        
app.run()