import numpy as np
import cv2
from keras.layers import Conv2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import MaxPooling2D, Activation, Dropout
# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
class CNNDuraiton():
    model = Sequential()
    def __init__():
        nClasses = 10

        model = Sequential()
        model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(70,30,3)))
        #model.add(Conv2D(32, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
        #model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
        #model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Flatten())
        model.add(Dense(512, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(nClasses, activation='softmax'))

        model.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])



        train_datagen = ImageDataGenerator(
        rescale = 1./255,
        # shear_range = 0.2,
        # zoom_range = 0.2,
        # horizontal_flip = True
        )

        test_datagen = ImageDataGenerator(
        rescale = 1./255
        )
        training_set = train_datagen.flow_from_directory('train_data1',
        target_size = (70, 30),
        batch_size = 32,
        class_mode = 'categorical')

        test_set = test_datagen.flow_from_directory('test_data1',
        target_size = (70, 30),
        batch_size = 32,
        class_mode = 'categorical')

        model.fit_generator(training_set,
        steps_per_epoch = 503,
        epochs = 2,
        validation_data = test_set,
        validation_steps = 210)
        CNNDuraiton.model = model


    def checkLength(path):
        model = CNNDuraiton.model
        img = cv2.imread(path)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.bitwise_not(gray_image)
        cv2.imwrite('bitwtest.png', img)
        test_image = load_img('bitwtest.png', target_size=(70, 30))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)

        print (result)
        resMax = result[0][0]
        pred = 'n1-1'
        if resMax < result[0][1]:
            resMax = result[0][1]
            pred = 'n1-16'
        if resMax < result[0][2]:
            resMax = result[0][2]
            pred = 'n1-2'
        if resMax < result[0][3]:
            resMax = result[0][3]
            pred = 'n1-4'
        if resMax < result[0][4]:
            resMax = result[0][4]
            pred = 'n1-8'
        if resMax < result[0][5]:
            resMax = result[0][5]
            pred = 'p1-1'
        if resMax < result[0][6]:
            resMax = result[0][6]
            pred = 'p1-16'
        if resMax < result[0][7]:
            resMax = result[0][7]
            pred = 'p1-2'
        if resMax < result[0][8]:
            resMax = result[0][8]
            pred = 'p1-4'
        if resMax < result[0][9]:
            resMax = result[0][9]
            pred = 'p1-8'
        print (resMax, pred)

# Part 3 - Making new predictions

#
# checkLength('images/predict/1-2.png')
# print('---should be n1-2---')
# checkLength('images/predict/1-16.png')
# print('---should be n1-16---')
# checkLength('images/predict/a3.jpg')
# print('---should be n1-2---')
# checkLength('images/predict/a4_test.png')
# print('---should be n1-8---')
# checkLength('images/predict/cela_pauza.png')
# print('---should be p1-1---')
# checkLength('images/predict/cetvrtina_pauze.png')
# print('---should be p1-4---')
# checkLength('images/predict/d4.png')
# print('---should be n1-4---')
# checkLength('images/predict/len1-4.png')
# print('---should be n1-4---')
# checkLength('images/predict/osmina_pauze.png')
# print('---should be p1-8---')
# checkLength('images/predict/pause1-2.png')
# print('---should be p1-2---')
# checkLength('images/predict/pause1-4.png')
# print('---should be p1-4---')
# checkLength('images/predict/pola_pauze.png')
# print('---should be p1-2---')
