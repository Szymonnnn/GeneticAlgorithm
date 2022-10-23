import random

def swap(cities_list_input, logger):
    cities_list= cities_list_input.copy()
    pos1 = random.randint(0, len(cities_list) - 1)
    pos2 = random.randint(0, len(cities_list) - 1)
    logger.log("Pozycje" + str(pos1) + ", " + str(pos2))
    tmp = cities_list[pos1]
    cities_list[pos1] = cities_list[pos2]
    cities_list[pos2] = tmp
    logger.log("Wynik " + str(cities_list))
    return cities_list

def inverse(cities_list_input):
    cities_list = cities_list_input.copy()
    pos1 = random.randint(0, len(cities_list) - 1)
    pos2 = random.randint(0, len(cities_list) - 1)
    if pos2 < pos1:
        pos_tmp = pos1
        pos1 = pos2
        pos2 = pos_tmp
    j = pos2
    for i in range(pos1, pos2):
        tmp = cities_list[i]
        cities_list[i] = cities_list[j]
        cities_list[j] = tmp
        j = j - 1
    return cities_list