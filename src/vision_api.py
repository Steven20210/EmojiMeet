import os, io, base64
from google.cloud import vision
import base64

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
path = "steven_picture.jpg"
temp_path = "temp.jpg"
client = vision.ImageAnnotatorClient()
#
with io.open(path, 'rb') as image_file:
    content = image_file.read()



def detect_faces(contents):

    # Creates jpg of img
    contents = contents.replace('data:image/png;base64,', '')
    f = open("temp.jpg", "wb")
    f.write(base64.b64decode(contents))
    f.close()

    # Opens the image
    with io.open(temp_path, 'rb') as face_file:
        byte_data = face_file.read()

    image = vision.Image(content=byte_data)

    response = client.face_detection(image=image)

    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    emotion = ""
    print(faces)
    for face in faces:
        print(likelihood_name[face.anger_likelihood])
        if (likelihood_name[face.anger_likelihood] == "VERY_LIKELY") or (likelihood_name[face.anger_likelihood] == "LIKELY") \
                or (likelihood_name[face.anger_likelihood] == "POSSIBLE"):
            emotion = "angry"
        elif (likelihood_name[face.joy_likelihood] == "VERY_LIKELY") or (likelihood_name[face.joy_likelihood] == "LIKELY")\
                or (likelihood_name[face.joy_likelihood] == "POSSIBLE"):
            emotion = "joy"
        elif (likelihood_name[face.surprise_likelihood] == "VERY_LIKELY") or (likelihood_name[face.surprise_likelihood] == "LIKELY")\
                or (likelihood_name[face.surprise_likelihood] == "POSSIBLE"):
            emotion = "surprise"
        elif (likelihood_name[face.sorrow_likelihood] == "VERY_LIKELY") or (likelihood_name[face.sorrow_likelihood] == "LIKELY") \
                or (likelihood_name[face.sorrow_likelihood] == "POSSIBLE"):
            emotion = "sorrow"
        else:
            emotion = "unknown"

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return emotion


# detect_faces(content)