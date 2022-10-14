tsp_file = open("TSP/berlin52.tsp", "r")
population_size = 4

#Wczytanie nagłówka
from head_reader import HeadReader
HeadReader.read(tsp_file)

#Wczytanie wartości
from cities_reading import CitiesReading
cities_list = CitiesReading.read(tsp_file)

#Pomiar jakości rozwiązania
from road_length import RoadLength
length = RoadLength.count(cities_list)
print(length)

#Inicjalizacja populacji
from city import city
population = city.population_initialization(city, cities_list, population_size)
print(len(population))
for i in range(population_size):
    print(RoadLength.count(population[i]))

#print(len(cities_list))