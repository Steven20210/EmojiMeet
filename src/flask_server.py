from flask import Flask, render_template, request
from vision_api import detect_faces
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@cross_origin()

@app.route('/', methods=["GET", "POST"])
def index():
    json_mood = {}
    if request.method == 'POST':
        # Fetch Form data
        json_data = request.json
        # print(json_data)
        img_data = json_data['image']
        mood = detect_faces(img_data)

        json_mood = {"mood": mood}
        print("success")
        return "success"


    if request.method == 'GET':
        return json_mood

#absl-py was originally 0.9
# deleted pywin32 from config

if __name__ == '__main__':
    app.run(debug=True)