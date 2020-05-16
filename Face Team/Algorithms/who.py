from PIL import Image
import os
import face_recognition


wanted_face = face_recognition.load_image_file('alexandra.jpg')
wanted_face_encoding = face_recognition.face_encodings(wanted_face)[0]
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i=Image.open(f)
        fn, fext = os.path.splitext(f)
        check_image = face_recognition.load_image_file(f)

        try:
            #wanted_face_encoding = face_recognition.face_encodings(wanted_image)[0]
            check_face_encoding = face_recognition.face_encodings(check_image)[0]
            #unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        except IndexError:
            print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
            quit()

        results = face_recognition.compare_faces(check_face_encoding, wanted_face_encoding)

print("Is the unknown face a picture of Biden? {}".format(results))
print("Is the unknown face a picture of Obama? {}".format(results))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))


    