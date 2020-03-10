import random
import numpy as np


def initialize(p_zero, N):
    the_map = np.zeros((N, N))
    for i in range(0, N):
        for j in range(0, i):
            random_value = round(random.random() * 100, 2)
            if random_value > p_zero:
                the_map[i][j] = random_value
                the_map[j][i] = random_value
    #print(the_map)
    return the_map


def create_new_member(max_route_length, the_map):
    N = len(the_map)
    route_length = random.randint(2, max_route_length)
    route = np.zeros(route_length, type(int))
    route[0] = 0
    i = 1
    while i < route_length:
        end_node = random.randint(0, N - 1)
        previouse_node = int(route[i - 1])
        weight = int(the_map[previouse_node][end_node])
        if (weight != 0 and route[i - 1] != end_node):
            route[i] = end_node
            i += 1
    return route


def create_starting_population(max_route_length, number_of_new_member, the_map):
    population = []
    for i in range(0, number_of_new_member):
        population.append(create_new_member(max_route_length, the_map))

    return population

