from cmath import inf
import math

class RoadLength:
    def __init__(self) -> None:
        pass

    def count(cities_list):
        length = 0
        for n in range(0,len(cities_list)):
            if n != len(cities_list)-1:
                X = abs(cities_list[n].x - cities_list[n+1].x)
                Y = abs(cities_list[n].y - cities_list[n+1].y)
                length += math.sqrt(X*X + Y*Y)
            else:
                X = abs(cities_list[n].x - cities_list[0].x)
                Y = abs(cities_list[n].y - cities_list[0].y)
                length += math.sqrt(X*X + Y*Y)
        return length

    def count_from_matrix(cities_list, matrix):
        length = 0
        for i in range(len(cities_list) - 1):
            length += matrix[cities_list[i].lp - 1][cities_list[i+1].lp - 1]
        length += matrix[cities_list[-1].lp - 1][cities_list[0].lp - 1]
        return length

    def generate_matrix(cities_list):
        matrix = []
        for i in range(len(cities_list)):
            row = []
            for j in range(len(cities_list)):
                if i == j:
                    cost = float(inf)
                else:
                    x = abs(cities_list[i].x - cities_list[j].x)
                    y = abs(cities_list[i].y - cities_list[j].y)
                    cost = math.sqrt(x*x + y*y)
                row.append(cost)
            matrix.append(row)
        return matrix