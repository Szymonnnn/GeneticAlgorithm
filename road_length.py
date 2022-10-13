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