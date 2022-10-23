from reader import Reader
from controller import Controller
import selection
import crossover
from individual import Individual
import random
import mutation

population_size = 100
selection_pressure = 5
generations_number = 100
crossing_probability = 0.7
mutation_probability = 0.1

reader = Reader('TSP/berlin52.tsp')
cities_list = reader.read_file()
controller = Controller(cities_list)
population = controller.initialize_population_greedy(population_size)
best_solution = min(population)
logs_file = open('statistics.csv', 'w')
best = best_solution.cost
sum = 0
for individual in population:
    sum += individual.cost
avg = sum/len(population)
worst = max(population).cost
print("nr_pokolenia;najlepsza_ocena;srednia_ocena;najgorsza_ocena;;;", file = logs_file)
print("0;" + str(best) + ";" + str(avg) + ";" + str(worst) + ";;;", file = logs_file)


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
    best = tmp_best_solution.cost
    sum = 0
    for individual in population:
        sum += individual.cost
    avg = sum/len(population)
    worst = max(population).cost
    print(str(iteration + 1) + ";" + str(best) + ";" + str(avg) + ";" + str(worst) + ";;;", file = logs_file)
    if tmp_best_solution < best_solution:
        best_solution = tmp_best_solution

print('Znaleziono rozwiazanie: ' + str(best_solution))
