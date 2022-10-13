tsp_file = open("TSP/berlin52.tsp", "r")

from head_reader import HeadReader
HeadReader.read(tsp_file)

from cities_reading import CitiesReading
cities_list = CitiesReading.read(tsp_file)

from road_length import RoadLength
length = RoadLength.count(cities_list)
print(length)

import random
random.shuffle(cities_list)

length = RoadLength.count(cities_list)
print(length)

#print(len(cities_list))