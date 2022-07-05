from keras.models import load_model
import cv2
from PIL import Image, ImageOps
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
# Load the model
def scan():
    while True:
        
        success, image = cap.read()
        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # Replace this with the path to your image
        #image = Image.open('<IMAGE_PATH>')
        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        image=cv2.resize(image,(224,224))
        #size = (224, 224)
        #image = ImageOps.fit(image, size, Image.ANTIALIAS)

        #turn the image into a numpy array
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array

        # run the inference
        prediction = model.predict(data)
        #print(prediction)
        for i in prediction:
            if i[0] > 0.7:
                text ="dog"
                break
            if i[1] > 0.7:
                text ="Bandicoot"
                break
            if i[2] > 0.7:
                text ="Elephant"
                break
            if i[3] > 0.7:
                text ="Fox"
                break
            if i[4] > 0.7:
                text ="Indian crested porcupine"
                break
            if i[5] > 0.7:
                text ="Monkey"
                break
            if i[6] > 0.7:
                text ="Peacock"
                break
            if i[7] > 0.7:
                text ="Pig-Boar"
                break
            if i[8] > 0.7:
                text ="Tiger"
                break
            if i[9] > 0.7:
                text ="Cow"
                break
            if i[10] > 0.7:
                text ="goat"
                break
            if i[11] > 0.7:
                text ="hen"
                break
            if i[12] > 0.7:
                text ="Human"
                break
            print(text)
            image = cv2.resize(image,(500, 500))
            cv2.putText(image,text,(10,30),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,255,0),1)
        cv2.imshow('img',image)
        cv2.waitKey(1)