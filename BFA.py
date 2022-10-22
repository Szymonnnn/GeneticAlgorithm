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

def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact * i
    return fact

_i = factorial(len(cities_list))
#główna pętla
import itertools
for permutation in itertools.permutations(cities_list):
    przejscie_petli+=1
    solution = Individual(permutation)
    if(solution < best_solution):
        best_solution = solution
print(solution)