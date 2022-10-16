from city import *
class Reader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tsp_file = None

    def read_header(self):
        name = self.tsp_file.readline()
        name = name.split(" ", 1)
        type = self.tsp_file.readline()
        type = type.split(" ", 1)
        comment = self.tsp_file.readline()
        comment = comment.split(" ", 1)
        dimension = self.tsp_file.readline()
        dimension = dimension.split(" ", 1)
        edge_weight_type = self.tsp_file.readline()
        edge_weight_type = edge_weight_type.split(" ", 1)
        section = self.tsp_file.readline()
        print("NAME: " + name[1], end="")
    
    def read_data(self):
        city_list = []
        readlines = self.tsp_file.readline()
        while readlines != "EOF\n":
            city_data = readlines.split(" ")
            city_data[2] = city_data[2][:-1]
            miasto = city(city_data[0], city_data[1], city_data[2])
            city_list.append(miasto)
            readlines = self.tsp_file.readline()
        return city_list
    
    def read_file(self):
        self.tsp_file = open(self.file_name, "r")
        self.read_header()
        data = self.read_data()
        self.tsp_file.close()
        return data

if __name__ == '__main__':
    print("It is not main file")