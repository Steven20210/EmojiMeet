from flask import Flask, render_template, request
from vision_api import detect_faces
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # Fetch Form data
        json_data = request.json
        print(json_data)
        img_data = json_data['image']

        mood = detect_faces(img_data)

        json_mood = {"mood":
        mood}

        return json_mood


    if request.method == 'GET':
        return 'get request'

#absl-py was originally 0.9
# deleted pywin32 from config

if __name__ == '__main__':
    app.run()