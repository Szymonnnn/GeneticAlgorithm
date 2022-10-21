from reader import Reader
import controller
import selection
import crossover
from individual import Individual
import random

population_size = 100
selection_pressure = 3
generations_number = 1000
crossing_probability = 0.5
mutation_probability = 0.1

reader = Reader('TSP/berlin11_modified.tsp')
cities_list = reader.read_file()
controller = controller.Controller(cities_list)
population = controller.initialize_population(population_size)
best_solution = min(population)

for iteration in range(generations_number):
    old_population = population.copy()
    population.clear()
    tmp_best_solution = min(old_population)
    if tmp_best_solution < best_solution:
        best_solution = tmp_best_solution
    for i in range(population_size//2):
        parent1 = selection.tournament(old_population, selection_pressure)
        parent2 = selection.tournament(old_population, selection_pressure)
        if random.random() < crossing_probability:
            chromosome1, chromosome2 = crossover.order_crossover(parent1.cities_list, parent2.cities_list)
        else:
            chromosome1 = parent1.cities_list
            chromosome2 = parent2.cities_list
        population.append(Individual(chromosome1))
        population.append(Individual(chromosome2))