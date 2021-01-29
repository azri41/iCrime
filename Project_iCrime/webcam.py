from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from torchvision import datasets
from torch.utils.data import DataLoader
from PIL import Image
import cv2
import time
import os

mtcnn0 = MTCNN(image_size=240, margin=0, keep_all=False,
               min_face_size=40)  # keep_all=False
mtcnn = MTCNN(image_size=240, margin=0, keep_all=True,
              min_face_size=40)  # keep_all=True
resnet = InceptionResnetV1(pretrained='vggface2').eval()
# Using webcam recognize face

# loading data.pt file
load_data = torch.load(r"F:\UTeM\SEM 5\AIPM\Projects\iCrime\Project_iCrime\data.pt")
embedding_list = load_data[0]
name_list = load_data[1]

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        print("fail to grab frame, try again")
        break

    img = Image.fromarray(frame)
    img_cropped_list, prob_list = mtcnn(img, return_prob=True)

    if img_cropped_list is not None:
        boxes, _ = mtcnn.detect(img)

        for i, prob in enumerate(prob_list):
            if prob > 0.90:
                emb = resnet(img_cropped_list[i].unsqueeze(0)).detach()

                dist_list = []  # list of matched distances, minimum distance is used to identify the person

                for idx, emb_db in enumerate(embedding_list):
                    dist = torch.dist(emb, emb_db).item()
                    dist_list.append(dist)

                min_dist = min(dist_list)  # get minumum dist value
                min_dist_idx = dist_list.index(
                    min_dist)  # get minumum dist index
                # get name corrosponding to minimum dist
                name = name_list[min_dist_idx]

                box = boxes[i]

                original_frame = frame.copy()  # storing copy of frame before drawing on it

                if min_dist < 0.90:
                    frame = cv2.putText(
                        frame, name+' '+str(min_dist), (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)

                frame = cv2.rectangle(
                    frame, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)

    cv2.imshow("IMG", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:  # ESC
        print('Esc pressed, closing...')
        break

    elif k % 256 == 32:  # space to save image
        print('Enter your name :')
        name = input()

        # create directory if not exists
        if not os.path.exists('photos/'+name):
            os.mkdir('photos/'+name)

        img_name = "photos/{}/{}.jpg".format(name, int(time.time()))
        cv2.imwrite(img_name, original_frame)
        print(" saved: {}".format(img_name))


cam.release()
cv2.destroyAllWindows()
