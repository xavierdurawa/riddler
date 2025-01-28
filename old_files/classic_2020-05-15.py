import numpy as np

def calc_minmax_dist(fn, *args):
    probs = args[0]
    for arg in args[1:]:
        probs = np.multiply.outer(probs, arg)
    
    new_dist = {}
    for idx, v in np.ndenumerate(probs):
        result = fn(idx) + 1
        if result in new_dist:
            new_dist[result] += v
        else:
            new_dist[result] = v
    return new_dist

def expectation(dist):
    total = 0
    for key, value in dist.items():
        total += (key+1) * value
    return total

n_sides = 20
d1 = d2 = [1/n_sides]*n_sides

min_dist = calc_minmax_dist(min, d1, d2)
max_dist = calc_minmax_dist(max, d1, d2)

adv_of_disadv = calc_minmax_dist(max, list(min_dist.values()), list(min_dist.values()))
disadv_of_adv = calc_minmax_dist(min, list(max_dist.values()), list(max_dist.values()))

print(expectation(adv_of_disadv))
print(expectation(disadv_of_adv))

