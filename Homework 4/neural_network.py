import numpy as np


class FFNeuralNetwork(object):
    def __init__(self, inputSize, hiddenSize, outputSize):
        """
        Purpose: Generates a Feed Forward Neural Network with three layers
        :param inputSize: First neural network layer that receives inputs from features
        :param hiddenSize: Second neural network layer that is between the input and output layers
        :param outputSize: The final layer that generates the desired results
        """

        # Weights
        self.W1 = np.random.uniform(-0.5, 0.5, size=(inputSize, hiddenSize))
        self.W2 = np.random.uniform(-0.5, 0.5, size=(hiddenSize, outputSize))

    def forward_propagation(self, input_features):
        self.z = np.dot(input_features, self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        o = self.sigmoid(self.z3)
        return o

    def sigmoid(self, s):
        """ Activation Function """
        s = np.clip(s, -6, 6)
        return 1/(1 + np.exp(-s))

    def sigmoid_prime(self, s):
        """ Derivative of sigmoid """
        return s * (1 - s)

    def backward_propagation(self, input_features, desired, actual):
        actual_error = desired - actual
        actual_delta = actual_error*self.sigmoid_prime(actual)

        z2_error = actual_delta.dot(self.W2.transpose())
        z2_delta = z2_error*self.sigmoid_prime(self.z2)

        self.W1 += input_features.transpose().dot(z2_delta)
        self.W2 += self.z2.transpose().dot(actual_delta)

    def train_neural_network(self, input_features, desired):
        o = self.forward_propagation(input_features)
        self.backward_propagation(input_features, desired, o)
         
    def determine_animal(self, result):
        animal = "dog"
        r = result[0]

        if result[1] > r:
            animal = "cat"
            r = result[1]
        if result[2] > r:
            animal = "dolphin"
            r = result[2]
        if result[3] > r:
            animal = "bird"

        return animal

