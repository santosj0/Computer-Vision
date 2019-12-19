import numpy as np
from sklearn import preprocessing as pre
from sklearn import decomposition as decom
import cv2

"""
Apparently we're going with a Game of Thrones theme
due to it just releasing recently. 
"""

""" Import the Test Case Images """
# Person 1 (Dragon Queen)
dq1 = cv2.imread('images/Dragon Queen 1.jpg')
dq1c = cv2.cvtColor(dq1, cv2.COLOR_RGB2BGR)
dq1g = cv2.cvtColor(dq1c, cv2.COLOR_BGR2GRAY)

dq2 = cv2.imread('images/Dragon Queen 2.jpg')
dq2c = cv2.cvtColor(dq2, cv2.COLOR_RGB2BGR)
dq2g = cv2.cvtColor(dq2c, cv2.COLOR_BGR2GRAY)

dq3 = cv2.imread('images/Dragon Queen 3.jpg')
dq3c = cv2.cvtColor(dq3, cv2.COLOR_RGB2BGR)
dq3g = cv2.cvtColor(dq3c, cv2.COLOR_BGR2GRAY)

dq4 = cv2.imread('images/Dragon Queen 4.jpg')
dq4c = cv2.cvtColor(dq4, cv2.COLOR_RGB2BGR)
dq4g = cv2.cvtColor(dq4c, cv2.COLOR_BGR2GRAY)

dq5 = cv2.imread('images/Dragon Queen 5.jpg')
dq5c = cv2.cvtColor(dq5, cv2.COLOR_RGB2BGR)
dq5g = cv2.cvtColor(dq5c, cv2.COLOR_BGR2GRAY)

# Person 2 (Missandei)
mi1 = cv2.imread('images/Missandei 1.jpg')
mi1c = cv2.cvtColor(mi1, cv2.COLOR_RGB2BGR)
mi1g = cv2.cvtColor(mi1c, cv2.COLOR_BGR2GRAY)

mi2 = cv2.imread('images/Missandei 2.jpg')
mi2c = cv2.cvtColor(mi2, cv2.COLOR_RGB2BGR)
mi2g = cv2.cvtColor(mi2c, cv2.COLOR_BGR2GRAY)

mi3 = cv2.imread('images/Missandei 3.jpg')
mi3c = cv2.cvtColor(mi3, cv2.COLOR_RGB2BGR)
mi3g = cv2.cvtColor(mi3c, cv2.COLOR_BGR2GRAY)

mi4 = cv2.imread('images/Missandei 4.jpg')
mi4c = cv2.cvtColor(mi4, cv2.COLOR_RGB2BGR)
mi4g = cv2.cvtColor(mi4c, cv2.COLOR_BGR2GRAY)

mi5 = cv2.imread('images/Missandei 5.jpg')
mi5c = cv2.cvtColor(mi5, cv2.COLOR_RGB2BGR)
mi5g = cv2.cvtColor(mi5c, cv2.COLOR_BGR2GRAY)

# Person 3 (Nichole)
n1 = cv2.imread('images/Nichole 1.jpg')
n1c = cv2.cvtColor(n1, cv2.COLOR_RGB2BGR)
n1g = cv2.cvtColor(n1c, cv2.COLOR_BGR2GRAY)

n2 = cv2.imread('images/Nichole 2.jpg')
n2c = cv2.cvtColor(n2, cv2.COLOR_RGB2BGR)
n2g = cv2.cvtColor(n2c, cv2.COLOR_BGR2GRAY)

n3 = cv2.imread('images/Nichole 3.jpg')
n3c = cv2.cvtColor(n3, cv2.COLOR_RGB2BGR)
n3g = cv2.cvtColor(n3c, cv2.COLOR_BGR2GRAY)

n4 = cv2.imread('images/Nichole 4.jpg')
n4c = cv2.cvtColor(n4, cv2.COLOR_RGB2BGR)
n4g = cv2.cvtColor(n4c, cv2.COLOR_BGR2GRAY)

n5 = cv2.imread('images/Nichole 5.jpg')
n5c = cv2.cvtColor(n5, cv2.COLOR_RGB2BGR)
n5g = cv2.cvtColor(n5c, cv2.COLOR_BGR2GRAY)

# Display all images
gray_arr = [dq1g, dq2g, dq3g, dq4g, dq5g, mi1g, mi2g, mi3g, mi4g, mi5g,
            n1g, n2g, n3g, n4g, n5g]
gray_arr = np.array(gray_arr)

""" Sklearn section """
# norm_x = pre.normalize(gray_arr.reshape(gray_arr.shape[0], gray_arr.shape[1]*gray_arr.shape[2]))
pca = decom.PCA(15)
flat = gray_arr.reshape(gray_arr.shape[0], gray_arr.shape[1]*gray_arr.shape[2])
flat = pre.normalize(flat)
pca.fit(flat)
print("scikit learn covariance: \n", pca.get_covariance().shape, end="\n\n")
print("scikit learn vectors: \n", pca.components_.shape, end="\n\n")
print("scikit learn transform: ", pca.transform(flat)[0][0])
