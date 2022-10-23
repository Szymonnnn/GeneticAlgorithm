from reader import Reader
from controller import Controller
import selection
import crossover
from individual import Individual
import random
import mutation
from logger import Logger

population_size = 10
selection_pressure = 3
generations_number = 10
crossing_probability = 0.75
mutation_probability = 0.1

reader = Reader('TSP/berlin11_modified.tsp')
cities_list = reader.read_file()
logger = Logger("logs.log")
controller = Controller(cities_list)
population = controller.initialize_population_greedy(population_size)
best_solution = min(population)
logger.log("Macierz kosztow:")
logger.log_array(controller.matrix)
logger.log("Poczatkowa populacja: ")
logger.log_population(population)
logger.log("Poczatkowe best_solution: " + str(best_solution))

for iteration in range(generations_number):
    logger.log("Iteracja " + str(iteration) + ".")
    old_population = population.copy()
    population.clear()
    for i in range(population_size//2):
        logger.log("Turniej 1")
        parent1 = selection.tournament(old_population, selection_pressure, logger)
        logger.log("Turniej 2")
        parent2 = selection.tournament(old_population, selection_pressure, logger)
        logger.log("Rodzice: " + str(parent1) + ", " + str(parent2))
        if random.random() < crossing_probability:
            logger.log("Krzyzujemy")
            chromosome1, chromosome2 = crossover.order_crossover(parent1.cities_list, parent2.cities_list, logger)
        else:
            logger.log("Przepisujemy")
            chromosome1 = parent1.cities_list
            chromosome2 = parent2.cities_list
        if random.random() < mutation_probability:
            logger.log("Mutujemy 1")
            chromosome1 = mutation.swap(chromosome1, logger)
        if random.random() < mutation_probability:
            logger.log("Mutujemy 2")
            chromosome2 = mutation.swap(chromosome2, logger)
        population.append(Individual(chromosome1))
        population[-1].evaluate(controller.matrix)
        population.append(Individual(chromosome2))
        population[-1].evaluate(controller.matrix)
    tmp_best_solution = min(population)
    logger.log("Nowa populacja: ")
    logger.log(population)
    logger.log("Najlepsze rozwiazanie w populacji: " + str(tmp_best_solution))
    if tmp_best_solution < best_solution:
        logger.log("ZAMIANA!")
        best_solution = tmp_best_solution

print('Znaleziono rozwiazanie: ' + str(best_solution))
logger.close_file()