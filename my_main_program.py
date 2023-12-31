import face_recognition
import os, sys
import numpy as np
import cv2

import math
import datetime

camera=0 
# camera = 0 -> default camera
# camera = 1 -> external USB camera

def face_confidence(face_distance, face_match_threshold=0.6):
    range = (1.0-face_match_threshold)
    linear_val = (1.0 - face_distance)/ (range*2.0)

    if face_distance > face_match_threshold:
        return(round(linear_val*100,2)) + '%'
    else:
        value = (linear_val +((1.0-linear_val)*math.pow((linear_val - 0.5)*2,0.2)))*100
        return str(round(value,2))+'%'

class FaceRecognition:
    face_locations= []
    face_encodings = []
    face_names = []
    known_face_enodings = []
    known_face_names = []
    process_current_frame = True

    def __init__(self):
        self.encode_faces()
        #encode faces
    
    def encode_faces(self):
        for image in os.listdir('faces'):
            face_image = face_recognition.load_image_file(f'faces/{image}')
            face_encoding  = face_recognition.face_encodings(face_image)[0]

            self.known_face_enodings.append(face_encoding)
            self.known_face_names.append(image.removesuffix('.png'))
        print(self.known_face_names)

    def run_recognition(self):
        video_capture=cv2.VideoCapture(camera)

        if not video_capture.isOpened():
            sys.exit('Video source not found...')

        while True:
            ret, frame = video_capture.read()

            if self.process_current_frame:
                small_frame = cv2.resize(frame, (0,0), fx = 0.25, fy=0.25)
                #rgb_small_frame = small_frame[:, :, ::-1]
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
                #Find all faces in the current frame
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []

                for face_encoding in self.face_encodings:
                    matches = face_recognition.compare_faces(self.known_face_enodings, face_encoding)
                    name = 'Unknown'
                    confidence = '??%'
                    # cv2.imwrite('faces/new_person.png',frame)
                    
                    face_distances = face_recognition.face_distance(self.known_face_enodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    try:
                        if matches[best_match_index]:
                            name = self.known_face_names[best_match_index]
                            confidence = face_confidence(face_distances[best_match_index])
                        else:
                            cv2.imwrite('faces/{}.png'.format(datetime.datetime.now().strftime('%Y-%m-%d-%H%M')),frame)
                            # fr = FaceRecognition()
                            self.known_face_names.clear()
                            self.encode_faces()
                    except:
                        pass
                        
                    self.face_names.append(f'{name}({confidence})')
    
            self.process_current_frame = not self.process_current_frame

            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                top *=4
                right *=4
                bottom *= 4
                left *=4

                cv2.rectangle(frame, (left, top),(right, bottom),(0,0,255),2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0,0,255),-1)
                cv2.putText(frame, name, (left+6, bottom -6),cv2.FONT_HERSHEY_DUPLEX, 0.6,(255,255,255),1)
            WINDOW_NAME = 'Face Recogntion (press \'q\' to exit)'
            cv2.imshow(WINDOW_NAME, frame)

            if cv2.waitKey(1) == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    fr = FaceRecognition()
    fr.run_recognition()