import face_recognition
import cv2
import requests
import json

#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# Get a reference to webcam #0 (the default one)
URL = 'https://www.sms4india.com/api/v1/sendCampaign'

count = 0


def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
    req_params = {
        'apikey': apiKey,
        'secret': secretKey,
        'usetype': useType,
        'phone': phoneNo,
        'message': textMessage,
        'senderid': senderId
    }
    return requests.post(reqUrl, req_params)


video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
first_image = face_recognition.load_image_file("images\Aslam.jpg")
first_face_encoding = face_recognition.face_encodings(first_image)[0]

# Load a second sample picture and learn how to recognize it.
second_image = face_recognition.load_image_file("images\Ravi.png")
second_face_encoding = face_recognition.face_encodings(second_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    first_face_encoding,
    second_face_encoding
]
known_face_names = [
    "Aslam",
    "Ravi Teja"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding)
            name = "unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (255, 255, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 1.0, (0, 255, 0), 1)
        count += 1
    # Display the resulting image
    cv2.imshow('Video', frame)

    if count==1:
        print("Found")
    
    # Hit 'q' on the keyboard to quit!
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('c'):
        print(count)
        
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        print(count," sms sent")
        # response = sendPostRequest('https://www.sms4india.com/api/v1/sendCampaign', 'XZCC10XND27COY2A3Q9ZO1WN3BGUTBI0',
        #                          '2I71MZFCVC2G618I', 'stage', '9676176764', 'shaikaslam340@gmail.com', 'Aslam fund at camera-1')
        # print(response.text)

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
