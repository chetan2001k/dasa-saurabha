from flask import Flask, Blueprint,render_template,request
from pymongo import MongoClient
import urllib.parse
main=Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return "dasaru1.html"


@main.route('/form1',methods =["GET", "POST"])
def form():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       song= request.form.get("naam")
       age = request.form.get("age")
       link=request.form.get("link")
       god=request.form.get("god")
       print(song)
       username = urllib.parse.quote_plus('admin')
       password = urllib.parse.quote_plus('CBK@2001')
       client=MongoClient("mongodb+srv://%s:%s@cluster0.bwv05gh.mongodb.net/"% (username, password),connect=False)
       db= client["data"]
       collection=db.test1
       di ={
            "song":song,
            "name":age,
            "link":link,
            "god":god
        }
       rec = collection.insert_one(di)
    return render_template('form1.html')

@main.route('/about')
def about():
    return "hello"


@main.route('/song')
def song():
    song= request.form.get("naam")
    age = request.form.get("name")
    link=request.form.get("link")
    god=request.form.get("god")
    print(song)
    username = urllib.parse.quote_plus('admin')
    password = urllib.parse.quote_plus('CBK@2001')
    client=MongoClient("mongodb+srv://%s:%s@cluster0.bwv05gh.mongodb.net/"% (username, password),connect=False)
    db= client["data"]
    collection=db.test1
    di ={
            "song":song,
            "name":age,
            "link":link,
            "god":god
    }
    data = collection.find({},{"_id":0,"link":1})
    l=""
    for i in data:
        l=i
    print(l)
    data = collection.find({},{"_id":0,"song":1})
    t=""



    for i in data:
        t=i

    print(t)
    return render_template('song.html')

@main.route('/data')
def data():
    username = urllib.parse.quote_plus('admin')
    password = urllib.parse.quote_plus('CBK@2001')
    client=MongoClient("mongodb+srv://%s:%s@cluster0.bwv05gh.mongodb.net/"% (username, password),connect=False)
    db= client["data"]
    collection=db.test1
    data = collection.find_one({"link":"https://www.youtube.com/embed/fZLE4xi3X-c"})
    num=0

    # song=""
    # age=""  
    # link=""
    # god=""
    text=data['song'].split('\n')
    print(text)
    print(data['song'])
    return render_template('data.html',d=data,t=text)
  



