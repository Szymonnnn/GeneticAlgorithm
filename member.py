class Member:
    def __init__(self, cities_list, costs_matrix):
        self.chromosome = cities_list.copy()
        self.cost = self.count_length(self, cities_list, costs_matrix)

    def count_length(self, cities_list, matrix):
        length = 0
        for i in range(len(cities_list) - 1):
            length += matrix[cities_list[i].lp - 1][cities_list[i+1].lp - 1]
        length += matrix[cities_list[-1].lp - 1][cities_list[0].lp - 1]
        return length

    def __repr__(self):
        return str(self.chomosome)