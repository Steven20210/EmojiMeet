from flask import Flask, render_template, request
from vision_api import detect_faces
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import json
app = Flask(__name__)
# database stuff
connection_stirng = "mongodb://localhost:27017"
client = MongoClient(connection_stirng)
db = client.get_database("emojiMeet")

collection = db.get_collection("emojiMeet")

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@cross_origin()


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # Fetch Form data
        json_data = request.json
        # print(json_data)
        img_data = json_data['image']
        mood = detect_faces(img_data)

        #update this
        collection.update_one({}, { "$set": {'mood': mood}})

        return "success"


    if request.method == 'GET':
        data = collection.find_one()
        mood_returned = data['mood']
        mood_json = {
            'mood': mood_returned
        }
        return mood_json

#absl-py was originally 0.9
# deleted pywin32 from config

if __name__ == '__main__':
    app.run(debug=True)