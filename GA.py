from reader import Reader
from road_length import RoadLength
from city import city
from selection import Selection
import crossover
import random
import mutation
import time

population_size = 100
selection_pressure = 3
generations_number = 1000
crossing_probability = 0.5
mutation_probability = 0.1

reader = Reader('TSP/berlin52.tsp')
cities_list = reader.read_file()
costs_matrix = RoadLength.generate_matrix(cities_list)
print(costs_matrix)
population = city.population_initialization(city, cities_list, population_size)
best_cost = float('inf')
best_solution = population[0]

start = time.time()
for iteration in range(generations_number):
    old_population = population.copy()

    road_lengths = []
    for i in range(population_size):
        road_lengths.append(RoadLength.count_from_matrix(old_population[i], costs_matrix))

    tmp_best_cost = min(road_lengths)
    if tmp_best_cost < best_cost:
        best_cost = tmp_best_cost
        best_solution = old_population[min(range(len(road_lengths)), key=road_lengths.__getitem__)]

    for i in range(population_size//2):
        parent1_id = Selection.tournament(road_lengths, selection_pressure)
        parent2_id = Selection.tournament(road_lengths, selection_pressure)

        if random.random() < crossing_probability:
            offspring1, offspring2 = crossover.order_crossover(old_population[parent1_id], old_population[parent2_id])
        else:
            offspring1 = old_population[parent1_id]
            offspring2 = old_population[parent2_id]

        if random.random() < mutation_probability:
            offspring1 = mutation.inverse(offspring1)
        if random.random() < mutation_probability:
            offpsring2 = mutation.inverse(offspring2)

        population.append(offspring1)
        population.append(offspring2)
end = time.time()
print('Czas wykonania' + str(end - start))
print(city.print_representation(best_solution))
print('Znaleziony koszt: ' + str(best_cost))