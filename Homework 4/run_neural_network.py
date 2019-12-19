
import cv2
import src.functions as func
import src.neural_network as nn
import numpy as np
from matplotlib import pyplot as plt

""" Import Section """
# Dog Imports
dog1 = cv2.imread('images/dog1.png')
dog1 = cv2.threshold(dog1, 127, 255, cv2.THRESH_BINARY_INV)[1]
dog2 = cv2.imread('images/dog2.png')
dog2 = cv2.threshold(dog2, 127, 255, cv2.THRESH_BINARY_INV)[1]
dog3 = cv2.imread('images/dog3.png')
dog3 = cv2.threshold(dog3, 127, 255, cv2.THRESH_BINARY_INV)[1]
dog4 = cv2.imread('images/dog4.png')
dog4 = cv2.threshold(dog4, 127, 255, cv2.THRESH_BINARY_INV)[1]
dog5 = cv2.imread('images/dog5.png')
dog5 = cv2.threshold(dog5, 127, 255, cv2.THRESH_BINARY_INV)[1]
dog_arr = [dog1, dog2, dog3, dog4, dog5]

# Cat Imports
cat1 = cv2.imread('images/cat1.png')
cat1 = cv2.threshold(cat1, 127, 255, cv2.THRESH_BINARY_INV)[1]
cat2 = cv2.imread('images/cat2.png')
cat2 = cv2.threshold(cat2, 127, 255, cv2.THRESH_BINARY_INV)[1]
cat3 = cv2.imread('images/cat3.png')
cat3 = cv2.threshold(cat3, 127, 255, cv2.THRESH_BINARY_INV)[1]
cat4 = cv2.imread('images/cat4.png')
cat4 = cv2.threshold(cat4, 127, 255, cv2.THRESH_BINARY_INV)[1]
cat5 = cv2.imread('images/cat5.png')
cat5 = cv2.threshold(cat5, 127, 255, cv2.THRESH_BINARY_INV)[1]
cat_arr = [cat1, cat2, cat3, cat4, cat5]

# Bird Imports
bird1 = cv2.imread('images/bird1.png')
bird1 = cv2.threshold(bird1, 127, 255, cv2.THRESH_BINARY_INV)[1]
bird2 = cv2.imread('images/bird2.png')
bird2 = cv2.threshold(bird2, 127, 255, cv2.THRESH_BINARY_INV)[1]
bird3 = cv2.imread('images/bird3.png')
bird3 = cv2.threshold(bird3, 127, 255, cv2.THRESH_BINARY_INV)[1]
bird4 = cv2.imread('images/bird4.png')
bird4 = cv2.threshold(bird4, 127, 255, cv2.THRESH_BINARY_INV)[1]
bird5 = cv2.imread('images/bird5.png')
bird5 = cv2.threshold(bird5, 127, 255, cv2.THRESH_BINARY_INV)[1]
bird_arr = [bird1, bird2, bird3, bird4, bird5]

# Dolphin Imports
dolphin1 = cv2.imread('images/dolphin1.png')
dolphin1 = cv2.threshold(dolphin1, 127, 255, cv2.THRESH_BINARY_INV)[1]
dolphin2 = cv2.imread('images/dolphin2.png')
dolphin2 = cv2.threshold(dolphin2, 127, 255, cv2.THRESH_BINARY_INV)[1]
dolphin3 = cv2.imread('images/dolphin3.png')
dolphin3 = cv2.threshold(dolphin3, 127, 255, cv2.THRESH_BINARY_INV)[1]
dolphin4 = cv2.imread('images/dolphin4.png')
dolphin4 = cv2.threshold(dolphin4, 127, 255, cv2.THRESH_BINARY_INV)[1]
dolphin5 = cv2.imread('images/dolphin5.png')
dolphin5 = cv2.threshold(dolphin5, 127, 255, cv2.THRESH_BINARY_INV)[1]
dolphin_arr = [dolphin1, dolphin2, dolphin3, dolphin4, dolphin5]

# Display all animals
plt.style.use('dark_background')
fig = plt.figure(figsize=(4, 5))
all_training = np.vstack([dog_arr, cat_arr, dolphin_arr, bird_arr])
for y in range(len(all_training)):
    for x in range(len(all_training[y])):
        plt.subplot(4, 5, (y*5)+(x+1))
        plt.imshow(all_training[y][x])
        plt.xticks([])
        plt.yticks([])
plt.show()

""" Feature Section """
# Dog Features
dog_cent = func.centroid_multi(dog_arr)
dog_peri = func.perimeter_multi(dog_arr)
dog_sect = func.extract_multi_sections(dog_peri, dog_cent)
dog_features = func.determine_multi_features(dog_sect, dog_cent)

# Cat Features
cat_cent = func.centroid_multi(cat_arr)
cat_peri = func.perimeter_multi(cat_arr)
cat_sect = func.extract_multi_sections(cat_peri, cat_cent)
cat_features = func.determine_multi_features(cat_sect, cat_cent)

# Dolphin Features
dolphin_cent = func.centroid_multi(dolphin_arr)
dolphin_peri = func.perimeter_multi(dolphin_arr)
dolphin_sect = func.extract_multi_sections(dolphin_peri, dolphin_cent)
dolphin_features = func.determine_multi_features(dolphin_sect, dolphin_cent)

# Bird Features
bird_cent = func.centroid_multi(bird_arr)
bird_peri = func.perimeter_multi(bird_arr)
bird_sect = func.extract_multi_sections(bird_peri, bird_cent)
bird_features = func.determine_multi_features(bird_sect, bird_cent)

# All Features
features = np.vstack([dog_features, cat_features, dolphin_features, bird_features])

# Show image with long/short distances
short, long = func.determine_features_position(bird_sect[0], bird_cent[0])
plt.style.use('dark_background')
fig = plt.figure(figsize=(4, 8))
for x in range(len(short)):
    a = [bird_cent[0][0], short[x][0]]
    b = [bird_cent[0][1], short[x][1]]
    c = [bird_cent[0][0], long[x][0]]
    d = [bird_cent[0][1], long[x][1]]

    plt.subplot(4, 8, x+1)
    plt.imshow(bird1)
    plt.plot(a, b, 'r-', c, d, 'b-')
    plt.plot(bird_cent[0][0], bird_cent[0][1], 'go')
    plt.plot(short[x][0], short[x][1], 'ro', long[x][0], long[x][1], 'bo')
    plt.xticks([])
    plt.yticks([])

plt.show()

""" Training Section """
# Building the neural network
nno = nn.FFNeuralNetwork(64, 16, 4)

# Index 0 is dog, index 1 is cat, index 2 is dolphin, index 3 is bird
# Expected answers
output = []
for x in range(20):
    if x < 5:
        output.append([1, 0, 0, 0])
    elif 5 <= x < 10:
        output.append([0, 1, 0, 0])
    elif 10 <= x < 15:
        output.append([0, 0, 1, 0])
    else:
        output.append([0, 0, 0, 1])

# Train neural network and gather loss from each iteration
loss = []
epoch = []
fea = features / np.amax(features, axis=0)
for x in range(1000):
    fp = nno.forward_propagation(fea)
    loss.append(np.mean(np.square(np.subtract(output, fp))))
    epoch.append(x+1)
    nno.backward_propagation(fea, output, fp)

# Display loss
plt.style.use('dark_background')
plt.plot(epoch, loss, 'b-')
plt.title("Loss vs. Epoch")
plt.xlabel('Epoch')
plt.ylabel("Loss")
plt.show()

""" Prediction section """
# Test Dog
tdog = cv2.imread('images/test-dog.png')
tdog = cv2.threshold(tdog, 127, 255, cv2.THRESH_BINARY_INV)[1]
tdcent = func.centroid(tdog)
tdperi = func.perimeter(tdog)
tdsect = func.extract_sections(tdperi, tdcent)
tdfeat = func.determine_features(tdsect, tdcent)
tdfeat = tdfeat / np.amax(tdfeat, axis=0)

fp = nno.forward_propagation(tdfeat)
animal = nno.determine_animal(fp)
print("Forward Propagation of test animal: ", fp)
print("The image you provided is a: ", animal)

# Test Cat
tcat = cv2.imread('images/test-cat.png')
tcat = cv2.threshold(tcat, 127, 255, cv2.THRESH_BINARY_INV)[1]
tccent = func.centroid(tcat)
tcperi = func.perimeter(tcat)
tcsect = func.extract_sections(tcperi, tccent)
tcfeat = func.determine_features(tcsect, tccent)
tcfeat = tcfeat / np.amax(tcfeat, axis=0)

fp = nno.forward_propagation(tcfeat)
animal = nno.determine_animal(fp)
print("Forward Propagation of test animal: ", fp)
print("The image you provided is a: ", animal)

plt.style.use('dark_background')
fig = plt.figure(figsize=(1, 2))
plt.subplot(1, 2, 1)
plt.imshow(tdog)
plt.xticks([])
plt.yticks([])
plt.subplot(1, 2, 2)
plt.imshow(tcat)
plt.xticks([])
plt.yticks([])
plt.show()



