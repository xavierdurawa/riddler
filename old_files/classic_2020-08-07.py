from math import factorial
from matplotlib import pyplot as plt

def choose(m, n):
    f = factorial
    return f(m) / (f(m-n)*f(n))

def binomial_generator(n, p):
    for i in range(n+1):
        yield choose(n, i) * p**i * p**(n-i)


num_nemotodes = 2
num_generations = 18
prob = .5
old_dist = {num_nemotodes: 1}
new_dist = {}
expected = []
pred_expected = []

for i in range(num_generations):
    for population, probability in old_dist.items():
        for n, p in enumerate(binomial_generator(population//2, prob)):
            new_population = n + population
            add_prob = p*probability
            if new_population in new_dist:
                new_dist[new_population] += add_prob
            else:
                new_dist[new_population] = add_prob

    old_dist = new_dist.copy()
    new_dist = {}

    ex = 0
    for v, p in old_dist.items():
        ex += v*p
    expected.append(ex)
    pred_expected.append(1.5**i*num_nemotodes)

# plt.plot(list(old_dist.keys()), list(old_dist.values()))
# plt.show()

print(expected)
t = [expected[i]/expected[i-1] for i in range(1, len(expected))]
print(t)
# plt.plot(expected, label='calculated')
# plt.plot(pred_expected, label='predicted')
# plt.legend()
# plt.show()