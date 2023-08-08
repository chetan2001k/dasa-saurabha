from flask_pymongo import PyMongo
from flask import Flask
import urllib.parse


app=Flask(__name__)

username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('CBK@2001')
app.config["MONGO_URI"]="mongodb+srv://%s:%s@cluster0.bwv05gh.mongodb.net/data"% (username, password)

db=PyMongo(app).db


@app.route("/")
def index():
    
    x=db.test1.insert_one({"name":"chetan","age":22})
    print(x)
    return "hello!"

app.run(debug=True)