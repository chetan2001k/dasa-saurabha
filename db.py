from pymongo import MongoClient
import urllib.parse

# creation of MongoClient
username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('CBK@2001')
client=MongoClient("mongodb+srv://%s:%s@cluster0.bwv05gh.mongodb.net/"% (username, password),connect=False)
db= client["data"]

collection=db.test1
di ={
    "name":"=ನಂಜನಗೂಡು ",
    "age":30
}
data=collection.find({"age":30})

for i in data:
    print(i)