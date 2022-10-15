import random

def swap(cities_list):
    pos1 = random.randint(0, len(cities_list) - 1)
    pos2 = random.randint(0, len(cities_list) - 1)
    print(pos1)
    print(pos2)
    tmp = cities_list[pos1]
    cities_list[pos1] = cities_list[pos2]
    cities_list[pos2] = tmp
    return cities_list