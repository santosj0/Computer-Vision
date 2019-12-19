import numpy as np
from matplotlib import pyplot as plt
from functions import pca, rmse, grayscale_image

""" Import the Training Images """
# Person 1 (Dragon Queen)
dq1 = grayscale_image('images/Dragon Queen 1.jpg')
dq2 = grayscale_image('images/Dragon Queen 2.jpg')
dq3 = grayscale_image('images/Dragon Queen 3.jpg')
dq4 = grayscale_image('images/Dragon Queen 4.jpg')
dq5 = grayscale_image('images/Dragon Queen 5.jpg')

# Person 2 (Missandei)
mi1 = grayscale_image('images/Missandei 1.jpg')
mi2 = grayscale_image('images/Missandei 2.jpg')
mi3 = grayscale_image('images/Missandei 3.jpg')
mi4 = grayscale_image('images/Missandei 4.jpg')
mi5 = grayscale_image('images/Missandei 5.jpg')

# Person 3 (Nichole)
n1 = grayscale_image('images/Nichole 1.jpg')
n2 = grayscale_image('images/Nichole 2.jpg')
n3 = grayscale_image('images/Nichole 3.jpg')
n4 = grayscale_image('images/Nichole 4.jpg')
n5 = grayscale_image('images/Nichole 5.jpg')

# Display all images
gray_arr = np.array([dq1, dq2, dq3, dq4, dq5, mi1, mi2, mi3, mi4, mi5,
                    n1, n2, n3, n4, n5])

plt.style.use('dark_background')
fig = plt.figure(figsize=(3,5))
for i in range(len(gray_arr)):
    plt.subplot(3, 5, i+1)
    plt.title(i)
    plt.imshow(gray_arr[i], cmap='gray', vmin=0, vmax=255)
    plt.xticks([])
    plt.yticks([])
plt.show()

""" Training """
y = []
for i in gray_arr:
    y.append(pca(i)[7])

""" Test Images """
# Dragon Queen Test
dqt = grayscale_image('images/Dragon Queen Test.jpg')
ydq = pca(dqt)[7]

# Missandei test
mit = grayscale_image('images/Missandei Test.jpg')
ymi = pca(mit)[7]

# Nichole test
nt = grayscale_image('images/Nichole Test.jpg')
yn = pca(nt)[7]

# Group images
test_group = np.array([dqt, mit, nt])

# Calculating the errors
errors = []
for i in y:
    errors.append([rmse(i, ydq), rmse(i, ymi), rmse(i, yn)])
errors = np.array(errors).transpose()
closest_image = [errors[0].argmin(), errors[1].argmin(), errors[2].argmin()]

""" Show Closest image """
titles = ['Dragon Queen Test', 'Missandei Test', 'Nichole Test']
plt.style.use('dark_background')
fig = plt.figure(figsize=(3, 2))
for i in range(3):
    plt.subplot(3, 2, (i*2)+1)
    plt.title(closest_image[i])
    plt.imshow(gray_arr[closest_image[i]], cmap='gray', vmin=0, vmax=255)
    plt.xticks([])
    plt.yticks([])
    plt.subplot(3, 2, (i*2)+2)
    plt.title(titles[i])
    plt.imshow(test_group[i], cmap='gray', vmin=0, vmax=255)
    plt.xticks([])
    plt.yticks([])
plt.show()
