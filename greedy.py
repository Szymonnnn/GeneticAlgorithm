from reader import Reader
from controller import Controller

reader = Reader('TSP/berlin52.tsp')
cities_list = reader.read_file()
controller = Controller(cities_list)
best_solution = controller.greedy_from_city(0)
for i in range(1, controller.problem_size):
    solution = controller.greedy_from_city(i)
    if solution < best_solution:
        best_solution = solution
print(best_solution)