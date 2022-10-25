from reader import Reader
from controller import Controller
import selection
import crossover
from individual import Individual
import random
import mutation

population_size = 100
selection_pressure = 3
generations_number = 1000
crossing_probability = 0.5
mutation_probability = 0.1

reader = Reader('TSP/berlin52.tsp')
cities_list = reader.read_file()
controller = Controller(cities_list)
population = controller.initialize_population_greedy(population_size)
best_solution = min(population)

for iteration in range(generations_number):
    old_population = population.copy()
    population.clear()
    for i in range(population_size//2):
        parent1 = selection.tournament(old_population, selection_pressure)
        parent2 = selection.tournament(old_population, selection_pressure)
        if random.random() < crossing_probability:
            chromosome1, chromosome2 = crossover.order_crossover(parent1.cities_list, parent2.cities_list)
        else:
            chromosome1 = parent1.cities_list
            chromosome2 = parent2.cities_list
        if random.random() < mutation_probability:
            chromosome1 = mutation.swap(chromosome1)
        if random.random() < mutation_probability:
            chromosome2 = mutation.swap(chromosome2)
        population.append(Individual(chromosome1))
        population[-1].evaluate(controller.matrix)
        population.append(Individual(chromosome2))
        population[-1].evaluate(controller.matrix)
    tmp_best_solution = min(population)
    if tmp_best_solution < best_solution:
        best_solution = tmp_best_solution

print('Znaleziono rozwiazanie: ' + str(best_solution))