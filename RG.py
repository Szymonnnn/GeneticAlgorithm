from reader import Reader
import random
from controller import Controller
from individual import Individual

repetitions_number = 10000000

reader = Reader('TSP/berlin11_modified.tsp')
cities = reader.read_file()
controller = Controller(cities)
cities_list = controller.generate_simple_list()

#pierwsze mieszanie zbioru
random.shuffle(cities_list)
solution = Individual(cities_list)
solution.evaluate(controller.matrix)
best_solution = solution

#główna pętla
for i in range(repetitions_number):
    random.shuffle(cities_list)
    solution = Individual(cities_list)
    solution.evaluate(controller.matrix)
    if(solution < best_solution):
        best_solution = solution
        print(i, solution)

print("Best solution: " + str(best_solution))