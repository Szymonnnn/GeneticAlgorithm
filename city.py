class city:
    def __init__(self, _lp, _x, _y):
        self.lp = int(_lp)
        self.x = float(_x)
        self.y = float(_y)

    def __str__(self):
        return "['" + str(self.lp) + "', '" + str(self.x) + "', '" + str(self.y) + "']"
    
    def __repr__(self):
        return "['" + str(self.lp) + "', '" + str(self.x) + "', '" + str(self.y) + "']"
    
    def list_randomization(cities_list):
        import random
        cities_list_copy = cities_list.copy()
        random.shuffle(cities_list_copy)
        return cities_list_copy
    
    def population_initialization(self, cities_list, amount):
        population = []
        for i in range(amount):
            population.append(self.list_randomization(cities_list))
        #print(population)
        return population
    
    def print_representation(cities_list):
        representation = ''
        for city in cities_list:
            representation = representation + str(city.lp) + ' '
        print(representation)