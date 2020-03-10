import matplotlib.pyplot as plt
import seaborn as sns

def plot_best(the_map, route, iteration_number):
    ax = sns.heatmap(the_map)

    x = [0.5] + [x + 0.5 for x in route[0:len(route) - 1]] + [len(the_map) - 0.5]
    y = [0.5] + [x + 0.5 for x in route[1:len(route)]] + [len(the_map) - 0.5]

    plt.plot(x, y, marker='o', linewidth=4, markersize=12, linestyle="-", color='white')
    # plt.savefig('images/new1000plot_%i.png' % (iteration_number), dpi=300)
    plt.show()