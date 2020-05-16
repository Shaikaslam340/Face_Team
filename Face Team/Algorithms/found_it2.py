import face_recognition
from PIL import Image
import os

obama_image = face_recognition.load_image_file("aslam.jpg")
try:
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()
#print(obama_face_encoding)
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i=Image.open(f)
        fn, fext = os.path.splitext(f)
        #i.save('found\{}.png'.format(fn))
        unknown_image = face_recognition.load_image_file(f)
        try:
            
            #obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        except IndexError:
            print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
            quit()
        
        known_faces = [
            obama_face_encoding,
            unknown_face_encoding
            ]
        #print(unknown_face_encoding)
        results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
#print(obama_face_encoding)
        
        img = face_recognition.load_image_file(f)
        face_locations = face_recognition.face_locations(img)
        print("I found {} face(s) in this photograph.".format(len(face_locations)))
        for face_location in face_locations:
            top, right, bottom, left = face_location
            print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
            face_image = img[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            pil_image.show()
            print(pil_image)
            '''
            try:
                pil_face_encoding = face_recognition.face_encodings(pil_image)[0]
            except IndexError:
                print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
                quit()
            known_faces_img = [
            obama_face_encoding,
            pil_face_encoding
            ]
            result = face_recognition.compare_faces(known_faces_img, obama_face_encoding)
            print(result)
            if result[0]==True and result[1]==True:
                image = Image.open(f)
            
                image.show()
            '''
        print(results)
        if results[0]==True and results[1]==True:
            image = Image.open(f)
            #image = face_recognition.load_image_file("faces.jpg")
            image.show()
print('done')