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
    print(the_map)
    return the_map


def create_new_member(max_route_length, N, the_map):
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
        population.append(create_new_member(max_route_length, len(the_map), the_map))

    return population


def fitness(route, the_map):
    score = 0
    for i in range(1, len(route)):
        score = score + the_map[route[i - 1]][route[i]]
    return score


def crossover(route_a, route_b):
    # we need to create two new routes based on these above(a,b)
    # we ll do it in the way to cut route_a on the same node where we cut route_b
    # so in that case we will have a correct route.
    print(route_a)
    common_el = set(route_a) & set(route_b)
    if (len(common_el) == 1):  # first el always will be 0 so that is one common el
        return (route_a, route_a)

    common_el.remove(0);
    cut_element = common_el.pop();
    index_a = np.where(route_a == cut_element)[0][0]
    index_b = np.where(route_b == cut_element)[0][0]

    if (index_a == 0 or index_a == len(route_a) - 1):
        return (route_a, route_b)

    if (index_b == 0 or index_b == len(route_b) - 1):
        return (route_a, route_b)

    route_a_first = route_a[0:index_a + 1]
    route_a_sec = route_b[index_b + 1:]
    new_A = np.concatenate((route_a_first, route_a_sec))

    route_b_first = route_b[0:index_b + 1]
    route_b_sec = route_a[index_a + 1:]
    new_B = np.concatenate((route_b_first, route_b_sec))

    return (new_A, new_B)


def mutate(route, probability, the_map):
    new_route = route[::]
    N = len(the_map)
    i = 1
    while i < len(new_route):
        if probability > random.random():
            end_node = random.randint(0, N - 1)
            previous_node = int(route[i - 1])
            weight = int(the_map[previous_node][end_node])
            if (weight != 0 and route[i - 1] != end_node):
                route[i] = end_node
                i += 1
    return route


def score_population(population, the_map):
    scores = []
    for i in range(0, len(population)):
        scores.append(fitness(population[i], the_map))

    return scores


def main():
    the_map = initialize(10, 50)
    population = create_starting_population(10, 30, the_map)

    for i in range(0, 1000):
        scores = score_population(population, the_map)

    print(scores)


# create_starting_population(10, 10, 10)
# a = np.array([0, 3, 4, 5, 6])
# b = np.array([0, 2, 7, 3])
# mutate(a, 0.4, initialize(10, 10))

main()
