import face_recognition
import os
import cv2
KNOWN_FACES_DIR = 'E:\Tutorial\Python\iCrime\Project_iCrime\known_faces'
print('Loading known faces...')
known_faces = []
known_names = []

# We oranize known faces as subfolders of KNOWN_FACES_DIR
# Each subfolder's name becomes our label (name)
for name in os.listdir(KNOWN_FACES_DIR):

    # Next we load every file of faces of known person
    for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):

        # Load an image
        image = face_recognition.load_image_file(
            f'{KNOWN_FACES_DIR}/{name}/{filename}')

        # Get 128-dimension face encoding
        # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
        tuple_encoding = face_recognition.face_encodings(image)
        # we check if there iis any face in the image
        if len(tuple_encoding) > 0:
            print(f'LOAD IMAGE IN THE TUPLE FOR FILTERATION = {filename}')
            encoding = (image)[0]
            print('LOAD SUCCESSFUL!')
            # if there is no face, we remove it from the folder
        else:
            print(f'no faces found at {filename}')
            print(f'removing {filename}....')
            os.remove(f'{KNOWN_FACES_DIR}/{name}/{filename}')
            print('FILE REMOVED!')

print("Filteration DONE!")
