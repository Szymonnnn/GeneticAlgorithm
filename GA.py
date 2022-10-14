tsp_file = open("TSP/berlin52.tsp", "r")
population_size = 5
selection_presure = 0

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

#vizualizacja ścieżki
#from roadmap import RoadMap
#RoadMap.plot(cities_list)

#Inicjalizacja populacji
from city import city
population = city.population_initialization(city, cities_list, population_size)
print(len(population))

#Lista długości dróg zainicjalizowanego zbioru
road_lengths = []
for i in range(population_size):
    road_lengths.append(RoadLength.count(population[i]))
print(road_lengths)

#Wybór osobników metodą ruletki
from roulette import Roulette
Roulette.roulette(road_lengths, selection_presure)

#print(len(cities_list))