import os, io, base64
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'src/ServiceAccountToken.json'
path = "src/steven_picture.jpg"
client = vision.ImageAnnotatorClient()

with io.open(path, 'rb') as image_file:
    content = image_file.read()

def encode_image(image):
  return base64.b64encode(image)

def detect_faces(contents):
    b = base64.b64decode(contents)
    # print(b)
    # print(content[:100])
    """Detects faces in an image."""
    result = encode_image(b)
    print(result[:100])

    # result = contents
    # print(result[:100])

    # content = base64.b64decode(contents)
    # with open('something.jpg', 'wb') as f:
    #     f.write(content)
    # print(type(contents))
    image = vision.Image(content=result)
    
    # image = base64.b64decode(contents)
    # png = base64.b64decode(contents)
    # f = open("temp.png", "w")
    # f.write(contents)
    # # f.write(png)
    # f.close()
    # image = r"temp.png"

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