import math
import random
import matplotlib.pyplot as plt

def choose(n, m):
    f = math.factorial
    return f(n) / (f(m)*f(n-m))

class War(object):

    def __init__(self, num_dead, num_alive, prob_dead_win):
        self.start_num_dead = num_dead
        self.start_num_alive = num_alive
        self.num_dead = num_dead
        self.num_alive = num_alive
        self.prob_dead_win = prob_dead_win
    
    def single_battle(self):
        if random.random() < self.prob_dead_win:
            self.num_dead += 1
            self.num_alive -=1
            return 'dead soldier wins'
        else:
            self.num_dead -= 1
            return 'living soldier wins'
    
    def whole_battle(self):
        while self.num_alive > 0 and self.num_dead > 0:
            self.single_battle()
            # Plot results for battle
            # plt.ylim(1,max(self.start_num_alive, self.start_num_dead)*2)
            # plt.bar(('dead', 'alive'), (self.num_dead, self.num_alive), color=('black', 'green'))
            # plt.pause(0.01)
            # plt.clf()
        if self.num_alive <= 0:
            return 'dead win'
        elif self.num_dead <= 0:
            return 'living win'
        else:
            return 'There is a bug in the code'
    
def run_simulation(num_dead, num_alive, prob_dead_win, num_trials):
    num_dead_wins = 0
    for i in range(num_trials):
        w = War(num_dead, num_alive, prob_dead_win)
        outcome = w.whole_battle()
        if outcome == 'There is a bug in the code':
            break
        elif outcome == 'dead win':
            num_dead_wins += 1
    
    return num_dead_wins

def probability_dead_win(num_dead, num_alive, prob_dead_win):
    ans = 0
    for i in range(num_dead+num_alive,2*num_alive+num_dead):
        ans += choose(2*num_alive+num_dead-1, i)
    return 1-ans/(4**(num_alive-1)*2**num_dead)

if __name__ == "__main__":
    num_trials = 1000
    prob_dead_win = .5
    num_living = 10
    sample_space = range(1, int(num_living/2)+1, 1)
    
    results = []
    analytic_results = []
    for n_d in sample_space:
        print(n_d)
        num_dead_wins = run_simulation(n_d, num_living, prob_dead_win, num_trials)
        results.append(num_dead_wins/num_trials)

        analytic_results.append(probability_dead_win(n_d, num_living, prob_dead_win))
    
    print(results)
    print(analytic_results)
    plt.plot(sample_space, results, sample_space, analytic_results)
    plt.show()
