from itertools import permutations
from reader import Reader
from road_length import RoadLength
from city import city
import time
from roadmap import RoadMap
import random

reader = Reader('TSP/berlin11_modified.tsp')
cities_list = reader.read_file()
random.shuffle(cities_list)

length = RoadLength.count(cities_list)
best_cities_list = cities_list.copy()

print(length)
old_length = length
przejscie_petli = 0

def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact * i
    return fact

_i = factorial(len(cities_list))
#główna pętla
import itertools
for i in itertools.permutations(cities_list):
    przejscie_petli+=1
    new_length = RoadLength.count(i)
    #print(new_length)
    if(new_length<length):
        length = new_length
        best_cities_list = i
        #RoadMap.plot(best_cities_list)
    if(przejscie_petli%100000 == 0):
        print(_i-przejscie_petli, "left, old:", round(old_length), "best:", length)
print(length)
#print(best_cities_list)

RoadMap.plot(best_cities_list)