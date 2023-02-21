import uuid
import os
from bson import ObjectId
from bson.json_util import dumps
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import pymongo
app = Flask(__name__)

# CORS(app, support_credentials=True)
CORS(app)


# client = MongoClient("mongodb+srv://ayush71120:<password>@self.s9euvud.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
# db = client.test
# MONGO_URI = os.environ.get('mongodb+srv://Self:34WqjLA3ATX2SBWk@self.s9euvud.mongodb.net/?retryWrites=true&w=majority')
# client = MongoClient(MONGO_URI)
# pass = 
Pass='mongodb+srv://ayush71120:ttssUlTeHJDLmNaw@self.s9euvud.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(Pass)
db = client.Class_Announcement
# db = client['Class_Announcement']
collection = db['Subjects']


@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if the username and password are correct
    if username == 'admin' and password == 'ayu123':
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})
    # VZO7NAxkbhtSk4qw


@app.route('/api', methods=['GET'])
def test():
    
        return "Working"
    # VZO7NAxkbhtSk4qw


@app.route('/api/addSubject', methods=['POST'])
def add_Subj():
    try:

        Subj = {'text': request.json['text']}

        status = db.Subjects.insert_one({
            "Subject": request.json['text']
        })
        new_Sub = collection.find_one({'_id': status.inserted_id})
        response = {
            '_id': str(new_Sub['_id']),
            'Subject': new_Sub['Subject'],
        }
        return response
    except Exception as e:
        return dumps({'error': str(e)})


@app.route('/api/addSubSubject', methods=['POST'])
def add_SubSubj():
    try:
        print(request.json['Parent'])
        status = db.Subparts.insert_one({
            "Heading": request.json['Heading'],
            "Body": request.json['Body'],
            "Link": request.json['Link'],
            "Parent_Id": request.json['Parent']
        })
        return "Working"
    except Exception as e:
        return dumps({'error': str(e)})


@app.route("/api/getAll", methods=["GET"])
def get_all():
    cursor = db.Subjects.find({})
    Subj_list = []
    for todo in cursor:
        todo["_id"] = str(todo["_id"])
        Subj_list.append(todo)
    return jsonify(Subj_list)


@app.route("/api/getAllsub/<id>", methods=["GET"])
def get_byid(id):
    print(id)
    cursor = db.Subparts.find({"Parent_Id": id})
    Subj_list = []
    for Sub in cursor:
        Sub["_id"] = str(Sub["_id"])
        Subj_list.append(Sub)
    return jsonify(Subj_list)
