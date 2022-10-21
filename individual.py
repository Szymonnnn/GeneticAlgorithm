class Individual:
    def __init__(self, cities_list):
        self.cities_list = cities_list.copy()
        self.cost = -1
    
    def evaluate(self, matrix):
        length = 0
        for i in range(len(self.cities_list) - 1):
            length += matrix[self.cities_list[i] - 1][self.cities_list[i+1] - 1]
        length += matrix[self.cities_list[-1] - 1][self.cities_list[0] - 1]
        self.cost = length

    def __repr__(self):
        return str(self.cities_list) + "=" + str(self.cost)

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __add__(self, other):
        return self.cost + other.cost
    
    def __radd__(self, other):
        return self.__add__(other)