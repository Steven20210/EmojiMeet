import os, io, base64
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
path = "steven_picture.jpg"
temp_path = "temp.jpg"
client = vision.ImageAnnotatorClient()
#
# with io.open(path, 'rb') as image_file:
#     content = image_file.read()



def detect_faces(contents):

    # Creates jpg of img
    f = open("temp.jpg", "w")
    f.write(contents)
    f.close()

    # Opens the image
    with io.open(path, 'rb') as face_file:
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
        print(face)
        if (face.anger_likelihood >= face.joy_likelihood) and (face.anger_likelihood >= face.surprise_likelihood):
            emotion = "angry"
        elif (face.joy_likelihood >= face.anger_likelihood) and (face.joy_likelihood >= face.surprise_likelihood):
            emotion = "joy"
        else:
            emotion = "surprise"

        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))


    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return emotion


# detect_faces(content)