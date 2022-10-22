import random
import math
from individual import Individual

class Controller:
    def __init__(self, cities_list):
        self.generate_matrix(cities_list)
        self.problem_size = len(cities_list)
        
    def randomize_list(cities_list):
        cities_list_copy = cities_list.copy()
        random.shuffle(cities_list_copy)
        return cities_list_copy

    def initialize_population(self, amount):
        population = []
        cities_list = list(range(self.problem_size))
        for i in range(amount):
            shuffled_list = cities_list.copy()
            random.shuffle(shuffled_list)
            population.append(Individual(shuffled_list))
            population[i].evaluate(self.matrix)
        return population

    def generate_matrix(self, cities_list):
        matrix = []
        for i in range(len(cities_list)):
            row = []
            for j in range(len(cities_list)):
                if i == j:
                    cost = float(math.inf)
                else:
                    x = abs(cities_list[i].x - cities_list[j].x)
                    y = abs(cities_list[i].y - cities_list[j].y)
                    cost = math.sqrt(x*x + y*y)
                row.append(cost)
            matrix.append(row)
        self.matrix = matrix