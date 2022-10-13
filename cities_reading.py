from city import *
class CitiesReading:
    def __init__(self) -> None:
        pass
    def read(tsp_file):
        city_list = []
        readlines = tsp_file.readline()
        while readlines != "EOF\n":

            city_data = readlines.split(" ")
            city_data[2] = city_data[2][:-1]
            miasto = city(city_data[0], city_data[1], city_data[2])

            city_list.append(miasto)
            readlines = tsp_file.readline()
        
        return city_list

