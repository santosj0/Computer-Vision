
import cv2
import math
import numpy as np

"""
Feature Section
"""
def centroid_image(image):
    """
    Purpose: Returns the image with a centroid mark
    :param image:
    :return:
    """

    out = image.copy()
    gray_image = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_image, 127, 255, 0)
    m = cv2.moments(thresh)
    cx = int(m["m10"] / m["m00"])
    cy = int(m["m01"] / m["m00"])
    cv2.circle(out, (cx, cy), 5, (255, 0, 0), -1)

    return out


def centroid(image):
    """
    Purpose: Returns the centroid of an image
    :param image:
    :return: X position and Y position of the centroid
    """

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_image, 127, 255, 0)
    m = cv2.moments(thresh)
    cx = int(m["m10"] / m["m00"])
    cy = int(m["m01"] / m["m00"])

    return cx, cy


def centroid_multi(image_arr):
    """
    Purpose: Generate the centroids for multiple images
    :param image_arr:
    :return:
    """
    z = []

    for x in image_arr:
        z.append(centroid(x))

    return np.array(z)


def perimeter_image(image):
    """
    Purpose: Returns an image with its perimeter highlighted
    :param image:
    :return:
    """

    out = image.copy()
    gray_image = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_image, 127, 255, 0)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(out, contours[0], -1, (0, 255, 0), 3)
    return out


def perimeter(image):
    """
    Purpose: Returns the perimeters pixels of an image. To access a perimeter,
    you have to go into the array twice. First to get the pixel, then the second
    to get into the X Y position.
    contours[0] = [[[x, y]], [[x1, y1]], ..., [[xd, yd]]]
    contour[0][1] = [[x1, y1]]
    contour[0][1][0] = [x1, y1]
    contour[0][1][0][1] = y1
    :param image:
    :return:
    """

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_image, 127, 255, 0)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    return contours[0]


def perimeter_multi(image_arr):
    """
    Purpose: Generate multiple perimeters for images
    :param image_arr:
    :return:
    """
    z = []

    for x in image_arr:
        z.append(perimeter(x))

    return np.array(z)


"""
Math Section
"""
def degree(point_a, point_b):
    vector2 = point_b - point_a
    vector1 = [0, -1]
    return math.degrees(math.atan2(vector2[1], vector2[0]) - math.atan2(vector1[1], vector1[0]))


def determine_distance(a1, b1):
    return math.sqrt(((a1[0]-b1[0])**2) + ((a1[1]-b1[1])**2))

"""
Grab Features Section
"""
def extract_sections(perimeter_arr, centroid):
    out = []

    # Get the degrees for each perimeter
    for y in perimeter_arr:
        deg = degree(centroid, y[0])
        out.append(deg)

    # Modify the negative degrees to positive
    for y in range(len(out)):
        if out[y] < 0:
            out[y] = out[y] + 360

    # Place each perimeter in its respective section
    sections = []
    for x in range(32):
        sections.append([])
        for y in range(len(out)):
            if x*11.25 <= out[y] <= (x+1)*11.25:
                sections[x].append(perimeter_arr[y][0])

    return sections


def extract_multi_sections(perimeter_arr, centroid_arr):
    """
    Purpose: Divides each perimeter into 32 sections
    :param perimeter_arr:
    :return:
    """
    z = []

    for x in range(len(perimeter_arr)):
        z.append(extract_sections(perimeter_arr[x], centroid_arr[x]))

    return np.array(z)


def determine_features_position(sections, centroid):
    sh = []
    lo = []

    for x in range(len(sections)):
        if len(sections[x]) > 0:
            short_dist = determine_distance(centroid, sections[x][0])
            dl = sections[x][0]
            long_dist = determine_distance(centroid, sections[x][0])
            ll = sections[x][0]
        else:
            dl = centroid
            ll = centroid

        for y in range(len(sections[x])):
            length = determine_distance(centroid, sections[x][y])
            if length < short_dist:
                short_dist = length
                dl = sections[x][y]
            if length > long_dist:
                long_dist = length
                ll = sections[x][y]

        sh.append(dl)
        lo.append(ll)

    return np.array(sh), np.array(lo)


def determine_features(sections, centroid):
    """
    Purpose: Get the 64 features that will run through the neural network. Each feature is the shortest and longest
    distance in each section
    :param sections: Arrays of pixel perimeter points
    :param centroid: Centroid of the image
    :return:
    """

    out = []

    for x in range(len(sections)):
        if len(sections[x]) > 0:
            short_dist = determine_distance(centroid, sections[x][0])
            long_dist = determine_distance(centroid, sections[x][0])
        else:
            short_dist = 0
            long_dist = 0

        for y in range(len(sections[x])):
            length = determine_distance(centroid, sections[x][y])
            if length < short_dist:
                short_dist = length
            if length > long_dist:
                long_dist = length

        out.append(short_dist)
        out.append(long_dist)

    return np.array(out).transpose()


def determine_multi_features(section_arr, centroid_arr):
    """
    Purpose: Get multiple 64 features based on multiple images
    :param section_arr:
    :param centroid_arr:
    :return:
    """
    z = []

    for x in range(len(section_arr)):
        z.append(determine_features(section_arr[x], centroid_arr[x]))

    return np.array(z)
