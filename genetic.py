import random
import numpy as np
import copy

def fitness(route, the_map):
    score = 0
    for i in range(1, len(route)):
        score = score + the_map[route[i - 1]][route[i]]
    return score


def crossover(route_a, route_b):
    # we need to create two new routes based on these above(a,b)
    # we ll do it in the way to cut route_a on the same node where we cut route_b
    # so in that case we will have a correct route.
    #print(route_a)
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


def pick_breeder(scores):
    array = np.array(scores)
    temp = array.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(array))

    fitness = [len(ranks) - x for x in ranks]

    cum_scores = copy.deepcopy(fitness)

    for i in range(1, len(cum_scores)):
        cum_scores[i] = fitness[i] + cum_scores[i - 1]

    probs = [x / cum_scores[-1] for x in cum_scores]

    rand = random.random()

    for i in range(0, len(probs)):
        if rand < probs[i]:
            return i