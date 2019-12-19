from sklearn import preprocessing as pre
import numpy as np
import cv2


def grayscale_image(image_path):
    """
    :param image_path: Path of the image respective to the folder
    :return: A grayscale image
    """
    return cv2.cvtColor(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)


def pca(image):
    """
    Input: image
    :return: flatten image, mean, A, covariance, eigenvalues, eigenvectors, y
    """

    # Flatten the image
    if image.ndim > 2:
        flat = image.reshape(image.shape[0], image.shape[1]*image.shape[2])
    else:
        flat = image.flatten().reshape(1, image.flatten().shape[0])

    # Normalize the image
    flat = pre.normalize(flat)

    # Get the mean
    mean = np.mean(flat, axis=1, keepdims=1)

    # Move vector to origin
    A = np.subtract(flat, mean)

    # Get the covariance matrix
    cov = np.dot(A, A.transpose()) * 1/A.shape[1]

    # Get the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(cov)

    # Map x to y
    full_y = eigenvectors.transpose().dot(A)
    full_y = np.flip(np.sort(full_y), axis=1)

    # Slimming down y and A to 20 features
    y = full_y.transpose()[:20].transpose()
    x = A.transpose()[:20].transpose()

    return flat, mean, A, cov, eigenvalues, eigenvectors, full_y, y, x


def rmse(observed, predicted):
    """ Root Mean Squared Error """
    return np.sqrt(np.mean((observed - predicted)**2))
