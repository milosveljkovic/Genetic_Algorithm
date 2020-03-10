from init import initialize,create_new_member,create_starting_population
from plot import plot_best
from genetic import score_population,fitness,crossover,pick_breeder,mutate
import numpy as np

def main():
    map_size = 100
    p_type = 10  # dont get when we will use it
    max_route_length = 150
    population_size = 30
    number_of_each_new_generation = 10
    number_of_couples = int((population_size - number_of_each_new_generation) / 2)
    probability = 0.05

    the_map = initialize(p_type, map_size)
    population = create_starting_population(max_route_length, population_size, the_map)
    last_distance = 1000000000

    for i in range(0, 100):
        scores = score_population(population, the_map)
        new_population = []

        best = population[np.argmin(scores)]
        number_of_moves = len(best)
        distance = fitness(best, the_map)

        if distance != last_distance:
            print('Iteration %i: Best so far is %i steps for a distance of %f' % (i, number_of_moves, distance))
            plot_best(the_map, best, i)

        for j in range(0, number_of_couples):
            new_route1, new_route2 = crossover(population[pick_breeder(scores)], population[pick_breeder(scores)])
            new_population.extend([new_route1, new_route2])

        # mutate the current members of new_population
        for j in range(0, len(new_population)):
            new_population[j] = mutate(new_population[j], probability, the_map)

        new_population.append(population[np.argmin(scores)])
        while len(new_population) < population_size:
            new_population.append(create_new_member(max_route_length, the_map))

        population = new_population[::]  # copy a values

main()