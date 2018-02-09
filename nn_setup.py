import numpy as np
import cv2
from keras.layers import Conv2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import MaxPooling2D, Activation, Dropout
# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from keras.layers.advanced_activations import LeakyReLU
from keras.models import load_model

class CNNValue():
    model = Sequential()
    def __init__():
        nClasses = 17

        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3), activation='linear', input_shape=(70, 30, 3), padding='same'))
        model.add(LeakyReLU(alpha=0.1))
        model.add(MaxPooling2D((2, 2), padding='same'))
        model.add(Conv2D(64, (3, 3), activation='linear', padding='same'))
        model.add(LeakyReLU(alpha=0.1))
        model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
        model.add(Conv2D(128, (3, 3), activation='linear', padding='same'))
        model.add(LeakyReLU(alpha=0.1))
        model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
        model.add(Flatten())
        model.add(Dense(512, activation='linear'))
        model.add(LeakyReLU(alpha=0.1))
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
        training_set = train_datagen.flow_from_directory('train_data',
        target_size = (70, 30),
        batch_size = 64,
        class_mode = 'categorical')

        test_set = test_datagen.flow_from_directory('test_data',
        target_size = (70, 30),
        batch_size = 32,
        class_mode = 'categorical')

        model.fit_generator(training_set,
        steps_per_epoch = 1407 ,
        epochs = 2,
        validation_data = test_set,
        validation_steps = 300 )
        CNNValue.model = model
        model.save('nnsetup.h5')

    def reloadModel():
        CNNValue.model = load_model('nnsetup.h5')
    def checkNote(path):
        model = CNNValue.model
        img = cv2.imread(path)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.bitwise_not(gray_image)
        cv2.imwrite('bitwtest.png', img)
        test_image = load_img('bitwtest.png', target_size=(70, 30))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)

        resMax = result[0][0]
        pred = 'a3'
        # if resMax < result[0][1]:
        #     resMax = result[0][1]
        #     pred = '1-2pause'
        # if resMax < result[0][2]:
        #     resMax = result[0][2]
        #     pred = '1-4pause'
        # if resMax < result[0][3]:
        #     resMax = result[0][3]
        #     pred = '1-8pause'
        # if resMax < result[0][4]:
        #     resMax = result[0][4]
        #     pred = '1-16pause'
        # if resMax < result[0][5]:
        #     resMax = result[0][5]
        #     pred = 'a3'
        if resMax < result[0][1]:
            resMax = result[0][1]
            pred = 'a4'
        if resMax < result[0][2]:
            resMax = result[0][2]
            pred = 'c4'
        if resMax < result[0][3]:
            resMax = result[0][3]
            pred = 'c5'
        if resMax < result[0][4]:
            resMax = result[0][4]
            pred = 'd4'
        if resMax < result[0][5]:
            resMax = result[0][5]
            pred = 'd5'
        if resMax < result[0][6]:
            resMax = result[0][6]
            pred = 'e4'
        if resMax < result[0][7]:
            resMax = result[0][7]
            pred = 'e5'
        if resMax < result[0][8]:
            resMax = result[0][8]
            pred = 'f4'
        if resMax < result[0][9]:
            resMax = result[0][9]
            pred = 'f5'
        if resMax < result[0][10]:
            resMax = result[0][10]
            pred = 'g4'
        if resMax < result[0][11]:
            resMax = result[0][11]
            pred = 'g5'
        if resMax < result[0][12]:
            resMax = result[0][12]
            pred = 'h3'
        if resMax < result[0][13]:
            resMax = result[0][13]
            pred = 'h4'
        if resMax < result[0][14]:
            resMax = result[0][14]
            pred = 'pauza'
        if resMax < result[0][15]:
            resMax = result[0][15]
            pred = 'taktica'
        if resMax < result[0][16]:
            resMax = result[0][16]
            pred = 'violinski kljuc'
       # print (resMax, pred)
        return pred
    # checkNote('images/predict/a4_test.png')
    # checkNote('images/predict/vkljuc_test.png')
    # checkNote('images/predict/taktica.png')
    # checkNote('images/predict/d4.png')
    # checkNote('images/predict/cetvrtina_pauze.png')
    # checkNote('images/predict/a3.jpg')
    # checkNote('images/predict/h3.jpg')
    # checkNote('images/predict/pola_pauze.png')
    # checkNote('images/predict/cela_pauza.png')
