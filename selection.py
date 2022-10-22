import random

def roulette(road_lengths, selection_presure):
    #inversion of road lengths
    road_lengths_inverse = []
    for i in range(len(road_lengths)):
        road_lengths_inverse.append(1/road_lengths[i].cost)

    Sum = sum(road_lengths_inverse)

    #I want sum of road_percentage to be 1.0
    roads_percentage = []
    for i in range(len(road_lengths)):
        roads_percentage.append(road_lengths_inverse.cost/Sum)
    
    #Increasing diversity acording to selection_presure
    for i in range(selection_presure):
        for j in range(len(roads_percentage)):
            roads_percentage[j] *= roads_percentage[j]
        Sum = sum(roads_percentage)
        for j in range(len(roads_percentage)):
            roads_percentage[j] = roads_percentage[j]/Sum

    #getting random number (0, 1) and picking correct individual/x2
    #it is possible to get same individual twice
    random_number = random.random()
    temp_number = 0
    outcome1 = 0
    outcome2 = 0

    for i in range(len(roads_percentage)):
        temp_number += roads_percentage[i]
        if(temp_number > random_number):
            outcome1 = i
            break
    
    random_number = random.random()
    temp_number = 0
    for i in range(len(roads_percentage)):
        temp_number += roads_percentage[i]
        if(temp_number > random_number):
            outcome2 = i
            break
    
    return road_lengths[outcome1], road_lengths[outcome2]

def tournament(population, selection_pressure):
    contestants = random.sample(range(len(population)), selection_pressure)
    winner = contestants[0]
    for contestant in contestants[1:]:
        if population[contestant] < population[winner]:
            winner = contestant
    return population[winner]