import face_recognition
from PIL import Image
import os

obama_image = face_recognition.load_image_file("obama.jpg")
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i=Image.open(f)
        fn, fext = os.path.splitext(f)
        #i.save('found\{}.png'.format(fn))
        unknown_image = face_recognition.load_image_file(f)
        try:
            #biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
            obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        except IndexError:
            print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
            quit()
        #print(obama_face_encoding)
        print()
        print(unknown_face_encoding)
        print()
print(obama_face_encoding)
print('done')