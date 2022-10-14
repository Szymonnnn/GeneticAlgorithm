class Roulette:
    def __init__(self) -> None:
        pass

    def roulette(road_lengths, selection_presure):
        road_lengths_inverse = []
        for i in range(len(road_lengths)):
            road_lengths_inverse.append(1/road_lengths[i])
        print(road_lengths_inverse)

        Sum = sum(road_lengths_inverse)

        roads_percentage = []
        for i in range(len(road_lengths)):
            roads_percentage.append(road_lengths_inverse[i]/Sum)
        print(roads_percentage)
        