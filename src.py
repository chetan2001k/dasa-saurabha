from flask import Flask, render_template,request
from pymongo import MongoClient
import urllib.parse

app = Flask(__name__,template_folder='Template')


@app.route('/form',methods =["GET", "POST"])
def index():
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
            "age":age,
            "link":link,
            "god":god
        }
       rec = collection.insert_one(di)
    return render_template('form1.html')

@app.route('/about')
def about():
    return render_template('index.html')


@app.route('/song')
def song():
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
            "age":age,
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

@app.route('/data')
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
  


if __name__ == '__main__':
    app.run(debug=True)