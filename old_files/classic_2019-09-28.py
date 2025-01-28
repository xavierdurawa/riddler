import random
import queue
import multiprocessing as mp

def avg(l):
    return sum(l)/len(l)

class Bases(object):
    def __init__(self):
        self.bases_queue = queue.Queue()
        list(map(self.bases_queue.put, ['empty']*3))
    
    def hit(self, num_bases):
        runner_progress = ['runner'] + ['empty']*(num_bases-1)
        list(map(self.bases_queue.put, runner_progress))
        runners_in = [self.bases_queue.get() for i in range(len(runner_progress))]
        rbis = runners_in.count('runner')
        return rbis

def points_scored(prob_single, prob_double, prob_triple, prob_homerun):
    prob_strikeout = 1 - (prob_single + prob_double + prob_triple + prob_homerun)
    assert prob_single + prob_double + prob_triple + prob_homerun + prob_strikeout == 1

    num_innings = 9
    num_out = 3

    inning = 1
    
    runs_scored = 0
    while inning <= num_innings:
        out = 0
        bases = Bases()
        while out < num_out:
            at_bat_outcome = random.choices(range(0,5), weights=[prob_strikeout, prob_single, prob_double, prob_triple, prob_homerun])[0]
            if at_bat_outcome == 0:
                out += 1
            else:
                runs_scored += bases.hit(at_bat_outcome)
        inning += 1
    return runs_scored

pool = mp.Pool(mp.cpu_count())

num_trials = 100000
results_moonwalkers = [pool.apply(points_scored, args=(.4, 0, 0, 0)) for i in range(num_trials)]
results_doubloons = [pool.apply(points_scored, args=(0, .2, 0, 0)) for i in range(num_trials)]
results_taters = [pool.apply(points_scored, args=(0, 0, 0, .1)) for i in range(num_trials)]

pool.close()

print('moonwalkers average: {0}\ndoubloons average: {1}\ntaters average: {2}'.format(avg(results_moonwalkers), 
                                                                                     avg(results_doubloons),
                                                                                     avg(results_taters)))