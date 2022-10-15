import random

def order_crossover(parent1, parent2):
    def make_offspring(parent1, parent2, positions):
        offspring = [None] * len(parent1)
        for i in range(positions[0], positions[1] + 1):
            offspring[i] = parent1[i]
        last_index = 0
        for i in range(len(offspring)):
            if offspring[i] is None:
                for j in range(last_index, len(parent2)):
                    if parent2[j] not in offspring:
                        offspring[i] = parent2[j]
                        last_index = j
                        break
        # if len(offspring) != len(set(offspring)) or None in offspring:
        #     print('WARNING: WRONG OFFSPRING')
        return offspring
        
    positions = random.sample(range(len(parent1)), 2)
    print("Positions")
    print(positions)
    if positions[1] < positions[0]:
        tmp = positions[1]
        positions[1] = positions[0]
        positions[0] = tmp
    return make_offspring(parent1, parent2, positions), make_offspring(parent2, parent1, positions)
    