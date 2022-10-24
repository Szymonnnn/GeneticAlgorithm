import random
import math
from individual import Individual

class Controller:
    def __init__(self, cities_list):
        self.generate_matrix(cities_list)
        self.problem_size = len(cities_list)

    def greedy_from_city(self, start_city):
        cities_list = [start_city]
        length = 0
        current_city = start_city
        cities_to_visit = list(range(self.problem_size))
        cities_to_visit.remove(start_city)
        while len(cities_to_visit) > 0:
            min_len = self.matrix[current_city][cities_to_visit[0]]
            next_city = cities_to_visit[0]
            for city in cities_to_visit[1::]:
                if self.matrix[current_city][city] < min_len:
                    min_len = self.matrix[current_city][city]
                    next_city = city
            cities_list.append(next_city)
            length += min_len
            cities_to_visit.remove(next_city)
        solution = Individual(cities_list)
        solution.cost = length
        return solution

    def initialize_population_greedy(self, amount):
        population = []
        for i in range(self.problem_size):
            population.append(self.greedy_from_city(i))
        if len(population) < amount:
            cities_list = list(range(self.problem_size))
        while len(population) < amount:
            random.shuffle(cities_list)
            solution = Individual(cities_list)
            solution.evaluate(self.matrix)
            population.append(solution)
        return population
        
    def randomize_list(cities_list):
        cities_list_copy = cities_list.copy()
        random.shuffle(cities_list_copy)
        return cities_list_copy

    def initialize_population_random(self, amount):
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

    def generate_simple_list(self):
        return list(range(self.problem_size))