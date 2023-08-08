from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

app = Flask(__name__,template_folder='Template')

# Connect to MongoDB
username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('CBK@2001')
client=MongoClient("mongodb+srv://%s:%s@cluster0.bwv05gh.mongodb.net/"% (username, password),connect=False)
db= client["data"]
collection=db.test1

@app.route('/')
def index():
    items = collection.find()  # Retrieve all items from the collection
    return render_template('i.html', i=items)

@app.route('/item/<item_id>')
def item_details(item_id):
    data = collection.find_one({'_id': ObjectId(item_id)})  # Query MongoDB using the item_id
    text=data['song'].split('\n')   
    return render_template('data.html',d=data,t=text)

if __name__ == '__main__':
    app.run(debug=True)

