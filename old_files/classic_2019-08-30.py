import random
import pandas as pd
import numpy as np
import math

def gen_seed_population(num_parent_pairs, num_troops, num_castles):
    num_parents = 2 * num_parent_pairs
    parents = []
    for p in range(num_parents):
        troop_assignments = np.zeros(10)
        for i in range(num_troops):
            n = random.choice(range(1,num_castles+1))
            troop_assignments[n-1] += 1
        parents.append(troop_assignments)
    return parents

def evaluate(historical_data, candidate):
    results = historical_data - candidate
    results = results.mask(results > 0, 1)
    results = results.mask(results < 0, -1)
    mult = [int(l.strip('Castle ')) for l in results.columns.values]
    results = results.multiply(mult, axis=1)
    results['Total'] = results.sum(axis=1)
    results['win?'] = results['Total'] > 0
    final_result = results['win?'].sum()
    return final_result

round2_results = pd.read_csv('/home/xavier/ProgramingProjects/Riddler/riddler_castles/castle-solutions-3.csv').drop('Why did you choose your troop deployment?', axis=1)
round2_result = round2_results.to_numpy()
num_solution_pairs = 2
num_troops = 100
num_castles = 10
num_generations = 5

parents = gen_seed_population(num_solution_pairs, num_troops, num_castles)

for g in range(num_generations):
    # Evaluate each of the parents
    parent_quality = [evaluate(round2_results, p) for p in parents]
    parent_data = list(zip(parents, parent_quality))

    # Order and then breed children
    children = []
    parent_data.sort(key=lambda x: x[1])
    for i in range(math.ceil(num_solution_pairs/2)):
        p1 = parent_data[2*i][0]
        p2 = parent_data[2*i + 1][0]
        c1 = pd.concat([p1, p2]).groupby(level=0).mean()
        # Mutate the other 3 children
        c2 = c1.sample(axis=0) + 5
        c2 = c2.sample(axis=0) - 5
        c3 = c2.sample(axis=0) + 10
        c3 = c3.sample(axis=0) - 10
        c4 = c3.sample(axis=0) + 20
        c4 = c4.sample(axis=0) - 20
        children.extend([c1, c2, c3, c4])
    print(parent_data[0][1])
    parents = children
