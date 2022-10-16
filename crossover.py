import random
def generate_positions(length):
    positions = random.sample(range(length), 2)
    if positions[1] < positions[0]:
        tmp = positions[1]
        positions[1] = positions[0]
        positions[0] = tmp
    return positions


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
        if len(offspring) != len(set(offspring)) or None in offspring:
            print('WARNING: WRONG OFFSPRING')
        return offspring
        
    positions = generate_positions(len(parent1))
    return make_offspring(parent1, parent2, positions), make_offspring(parent2, parent1, positions)

def partially_mapped_crossover(parent1, parent2):
    def make_offspring(parent1, parent2, positions):
        offspring = [None] * len(parent1)
        mappings = {}
        for i in range(positions[0], positions[1] + 1):
            offspring[i] = parent1[i]
            mappings[parent1[i]] = parent2[i]
        for i in range(len(offspring)):
            if offspring[i] is None:
                gene = parent2[i]
                while gene in offspring:
                    gene = mappings[gene]
                offspring[i] = gene
        if len(offspring) != len(set(offspring)) or None in offspring:
            print('WARNING: WRONG OFFSPRING')
        return offspring
    
    positions = generate_positions(len(parent1))
    return make_offspring(parent1, parent2, positions), make_offspring(parent2, parent1, positions)
