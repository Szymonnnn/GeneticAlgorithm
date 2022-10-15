tsp_file = open("TSP/berlin52.tsp", "r")
population_size = 10
selection_pressure = 3
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

#Inicjalizacja populacji
from city import city
population = city.population_initialization(city, cities_list, population_size)

#Lista długości dróg zainicjalizowanego zbioru
road_lengths = []
for i in range(population_size):
    road_lengths.append(RoadLength.count(population[i]))

#Wybór osobników metodą ruletki
from selection import Roulette
Parent1, Parent2 = Roulette.roulette(road_lengths, selection_pressure)

#wizualizacja ścieżki
#from roadmap import RoadMap
#RoadMap.plot(population[Parent1])
#RoadMap.plot(population[Parent2])