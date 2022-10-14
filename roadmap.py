import matplotlib.pyplot as plt
import numpy as np

class RoadMap:
    def __init__(self) -> None:
        pass

    def plot(cities_list):
        X = []
        Y = []

        for city in cities_list:
            X.append(city.x)
            Y.append(city.y)
        X.append(cities_list[0].x)
        Y.append(cities_list[0].y)

        #X = np.array(X)
        #Y = np.array(Y)
        plt.figure()
        plt.plot(X, Y, '-o')
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()