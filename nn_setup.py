import numpy as np
import cv2
from keras.layers import Conv2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import MaxPooling2D, Activation, Dropout
# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

# batch_size = 32
# img = load_img('images/train/nota1.bmp')  # this is a PIL image
# x = img_to_array(img)
# input_shape = x.shape
# nClasses = 10
#
#
# train_datagen = ImageDataGenerator(
#         rescale=1./255,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True)
#
# # this is the augmentation configuration we will use for testing:
# # only rescaling
# test_datagen = ImageDataGenerator(rescale=1./255)
#
# # this is a generator that will read pictures found in
# # subfolers of 'data/train', and indefinitely generate
# # batches of augmented image data
# train_generator = train_datagen.flow_from_directory(
#         'data/train',  # this is the target directory
#         target_size=(150, 150),  # all images will be resized to 150x150
#         batch_size=batch_size,
#         class_mode='categorical')  # since we use binary_crossentropy loss, we need binary labels
#
# # this is a similar generator, for validation data
# validation_generator = test_datagen.flow_from_directory(
#         'data/validation',
#         target_size=(150, 150),
#         batch_size=batch_size,
#         class_mode='categorical')
# model = Sequential()
# The first two layers with 32 filters of window size 3x3
# model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=input_shape))
# model.add(Conv2D(32, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))
#
# model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))
#
# model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))
#
# model.add(Flatten())
# model.add(Dense(512, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(nClasses, activation='softmax'))
# Initialising the CNN
# classifier = Sequential()
# # Step 1 - Convolution
# classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
# # Step 2 - Pooling
# classifier.add(MaxPooling2D(pool_size = (2, 2)))
# # Adding a second convolutional layer
# classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
# classifier.add(MaxPooling2D(pool_size = (2, 2)))
# # Step 3 - Flattening
# classifier.add(Flatten())
# # Step 4 - Full connection
# classifier.add(Dense(units = 128, activation = 'relu'))
# classifier.add(Dense(units = 1, activation = 'sigmoid'))
# # Compiling the CNN
# classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
# # Part 2 - Fitting the CNN to the images
# from keras.preprocessing.image import ImageDataGenerator
# train_datagen = ImageDataGenerator(rescale = 1./255,
# shear_range = 0.2,
# zoom_range = 0.2,
# horizontal_flip = True)
# test_datagen = ImageDataGenerator(rescale = 1./255)
# training_set = train_datagen.flow_from_directory('images/training_set',
# target_size = (64, 64),
# batch_size = 32,
# class_mode = 'categorical')
# test_set = test_datagen.flow_from_directory('images/test_set',
# target_size = (64, 64),
# batch_size = 32,
# class_mode = 'categorical')
# classifier.fit_generator(training_set,
# steps_per_epoch = 100,
# epochs = 2,
# validation_data = test_set,
# validation_steps = 100)
# # Part 3 - Making new predictions
# import numpy as np
# from keras.preprocessing import image
# test_image = image.load_img('images/predict/cat_or_dog_1.jpg', target_size = (64, 64))
# test_image = image.img_to_array(test_image)
# test_image = np.expand_dims(test_image, axis = 0)
# result = classifier.predict(test_image)
# #
# # if result[0][0] == 1:
# #     prediction = 'dog'
# # else:
# #     prediction = 'cat'
#
# print result
nClasses = 17

model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(70,30,3)))
#model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
#model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))

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
training_set = train_datagen.flow_from_directory('train_data',
target_size = (70, 30),
batch_size = 32,
class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('test_data',
target_size = (70, 30),
batch_size = 32,
class_mode = 'categorical')

model.fit_generator(training_set,
steps_per_epoch = 1562 ,
epochs = 2,
validation_data = test_set,
validation_steps = 364 )

def checkNote(path):
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
        pred = 'pauze'
    if resMax < result[0][15]:
        resMax = result[0][15]
        pred = 'taktica'
    if resMax < result[0][16]:
        resMax = result[0][16]
        pred = 'violinski kljuc'
    print (resMax, pred)

checkNote('images/predict/a4_test.png')
checkNote('images/predict/vkljuc_test.png')
checkNote('images/predict/taktica.png')
checkNote('images/predict/d4.png')
checkNote('images/predict/cetvrtina_pauze.png')
checkNote('images/predict/a3.jpg')
checkNote('images/predict/h3.jpg')
checkNote('images/predict/pola_pauze.png')
checkNote('images/predict/cela_pauza.png')
