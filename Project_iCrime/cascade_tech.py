import cv2
import face_recognition
import numpy as np
import os
import glob

face_encodings = []
faces_names = []

cur_direc = os.getcwd()
path = os.path.join(cur_direc, '/all_face')
list_of_files = [f for f in glob.glob(path+'*.jpg')]
number_files = len(list_of_files)
names = list_of_files.copy()


for i in range(number_files):
    globals()['image_{}'.format(i)] =
face_recognition.load_image_file(list_of_files[i])