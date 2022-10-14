tsp_file = open("TSP/berlin52.tsp", "r")
population_size = 10
selection_presure = 3
generations_number = 10

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
#print(len(population))

#Lista długości dróg zainicjalizowanego zbioru
road_lengths = []
for i in range(population_size):
    road_lengths.append(RoadLength.count(population[i]))
print(road_lengths)

#Wybór osobników metodą ruletki
from roulette import Roulette
Parent1, Parent2 = Roulette.roulette(road_lengths, selection_presure)
print(Parent1, Parent2)

#wizualizacja ścieżki
#from roadmap import RoadMap
#RoadMap.plot(population[Parent1])
#RoadMap.plot(population[Parent2])

#długość ścieżek osobników rodziców nowej populacji
print(RoadLength.count(population[Parent1]))
print(RoadLength.count(population[Parent2]))

#print(len(cities_list))