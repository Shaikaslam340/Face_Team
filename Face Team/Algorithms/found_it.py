import face_recognition
from PIL import Image
import os

obama_image = face_recognition.load_image_file("aslam.jpg")
try:
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()
print(obama_face_encoding)
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
        
        
        
        print(results)
        if results[0]==True and results[1]==True:
            image = Image.open(f)
            #image = face_recognition.load_image_file("faces.jpg")
            image.show()
print('done')