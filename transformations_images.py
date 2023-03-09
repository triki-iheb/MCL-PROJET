from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import cv2


class TransformationImageVoiture(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        # initialize an empty list to hold the image vectors
        image_vectors = []
        
        # loop through each image path
        for image_path in X:
            # read the image
            image = cv2.imread(image_path)
            # convert the image to grayscale
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # convert the image to a vector
            vector = grayscale_image.reshape(-1)
            # add the vector to the list
            image_vectors.append(vector)

        # convert the list of vectors to a numpy array and return it
        return np.array(image_vectors)
