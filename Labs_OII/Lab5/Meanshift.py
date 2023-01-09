import numpy as np
from numpy import genfromtxt
import numpy.random as rand
import matplotlib.pyplot as plt


class Mean_Shift:
    data = []

    def __init__(self, input_file, delimiter, radius):
        self.data = genfromtxt(input_file, delimiter=delimiter, dtype=None)
        self.radius = radius

    def shuffle(self):
        np.random.shuffle(self.data)

    def fix(self, k):
        for i in range(k, len(self.data)):
            self.data = np.delete(self.data, k, axis=0)

    def fit(self):
        centroids = {}

        for i in range(len(self.data)):
            centroids[i] = self.data[i]

        while True:
            new_centroids = []
            for i in centroids:
                in_bandwidth = []
                centroid = centroids[i]
                for featureset in self.data:
                    if np.linalg.norm(featureset - centroid) < self.radius:
                        in_bandwidth.append(featureset)

                new_centroid = np.average(in_bandwidth, axis=0)
                new_centroids.append(tuple(new_centroid))

            uniques = sorted(list(set(new_centroids)))

            prev_centroids = dict(centroids)

            centroids = {}
            for i in range(len(uniques)):
                centroids[i] = np.array(uniques[i])

            optimized = True

            for i in centroids:
                if not np.array_equal(centroids[i], prev_centroids[i]):
                    optimized = False
                if not optimized:
                    break

            if optimized:
                break

        self.centroids = centroids

        plt.scatter(self.data[:, 0], self.data[:, 1], color='r')
        print('Количество кластеров: ', len(self.centroids))

        for c in self.centroids:
            plt.scatter(self.centroids[c][0], self.centroids[c][1], color='black', marker='*', s=150)

        plt.show()
