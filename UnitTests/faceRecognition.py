import cv2
import face_recognition
import numpy as np
#download using cmd by  pip install numpy

cap = cap=cv2.VideoCapture()

Fatima_Face= face_recognition.load_image_file('fatima.jpg')
Factima_face_Encode = face_recognition.face_encodings(Fatima_Face)

p2_Face= face_recognition.load_image_file('p2.jpg')
p2_face_Encode = face_recognition.face_encodings(p2_Face)

#i
Known_faces = [Factima_face_Encode, p2_face_Encode]
known_Face_Names=['Fatima Kj', 'Janbaz Kha']

#Declaring some variables
Face_Encode_From_Cam = []
Face_Name_From_Cam = []

while True:
    ret, frame = cap.read()
    cv2.imshow('Camera',frame)
    #resizing the frame for better and face detection
    Small_Frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = Small_Frame[:,:,::-1]
    Face_Location_From_Cam = face_recognition.face_locations(rgb_small_frame)
    Face_Encode_From_Cam = face_recognition.face_encodings(rgb_small_frame, Face_Location_From_Cam)

    for face in Face_Encode_From_Cam:
        name="Unknown"
        face_compare=face_recognition.compare_faces(Known_faces,face)
        distance = face_recognition.face_distance(Known_faces)
        best_match_index=np.argmin(distance)
        if face_compare[best_match_index]:
            name=known_Face_Names[best_match_index]

        Face_Name_From_cam.append(name)

for (top, right, bottom,left), name in zip(Face_Location_From_Cam,Face_Name_From_)




    k = cv2.waitKey(10)
    if k%256==27:
        print('Closing...')
        break
