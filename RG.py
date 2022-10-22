from reader import Reader
from road_length import RoadLength
from city import city
import time
from roadmap import RoadMap
import random

repetitions_number = 10000000

reader = Reader('TSP/berlin52.tsp')
cities_list = reader.read_file()

#pierwsze mieszanie zbioru
random.shuffle(cities_list)
length = RoadLength.count(cities_list)
best_cities_list = cities_list.copy()

#główna pętla
for i in range(repetitions_number):
    old_cities_list = cities_list.copy()
    random.shuffle(cities_list)
    new_length = RoadLength.count(cities_list)
    if(new_length<length):
        length = new_length
        best_cities_list = cities_list.copy()
        print(i, length)

print(length)
#print(best_cities_list)

RoadMap.plot(best_cities_list)