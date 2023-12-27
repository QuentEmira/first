import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Creating an implementation of the k_means algorithm. Assumes that the input is give as a dataframe for now.
class k_means:
    def select_centroids(self):
        self.centroids = (self.X.sample(n=self.k))
    
    def euclidean(point,data):
        return np.sqrt(np.sum((point - data)**2, axis=1))

    def __init__(self,X,k=5,n_iter=5):
        self.k = k
        self.X = X
        self.select_centroids()
        self.n_iter = n_iter
    
    def show_centroids(self):
        plt.scatter(self.X["Latitude"],self.X["Longitude"],c='black')
        plt.scatter(self.centroids["Latitude"],self.centroids["Longitude"],c='red')
        plt.xlabel('Latitude')
        plt.ylabel('Longitude')
        plt.show()
    
    def form_cluster(self):
        