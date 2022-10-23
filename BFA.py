import itertools
from reader import Reader
import random
from controller import Controller
from individual import Individual

reader = Reader('TSP/berlin11_modified.tsp')
cities_list = reader.read_file()
controller = Controller(cities_list)
cities = list(range(controller.problem_size))
random.shuffle(cities)
best_solution = Individual(cities)
best_solution.evaluate(controller.matrix)

print(best_solution)
przejscie_petli = 0

#główna pętla
for permutation in itertools.permutations(cities_list):
    przejscie_petli+=1
    solution = Individual(permutation)
    if(solution < best_solution):
        best_solution = solution
print(solution)