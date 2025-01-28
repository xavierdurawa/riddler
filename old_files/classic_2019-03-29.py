import random
from collections import deque, Counter, namedtuple
from matplotlib import pyplot

class Modifiable_Cycle(object):
    def __init__(self, items=()):
        self.deque = deque(items)
        self.length = len(self.deque)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.deque:
            raise StopIteration
        item = self.deque.popleft()
        self.deque.append(item)
        return item
    
    next = __next__

    def delete_current(self):
        self.deque.pop()
        self.length -= 1
    
    def get_length(self):
        return self.length

class Spelling_Bee(object):
    def __init__(self, players):
        """Create a Spelling Bee object

        Arguments:
        players -- a list of the players as named tuples
        """
        assert len(players) > 1, "One or more players must be in the Spelling Bee"
        self.players = players

    def compete(self):
        remaining_players = Modifiable_Cycle(self.players)
        for p in remaining_players:
            if remaining_players.get_length() == 1:
                return p
            elif random.random() > p.prob_correct:
                remaining_players.delete_current()
            else:
                continue

    def run_trials(self, num_trials):
        cnt = Counter()
        for t in range(num_trials):
            cnt[self.compete()] += 1
        return cnt

if __name__ == "__main__":
    
    Player = namedtuple('Player', ['name', 'prob_correct'])
    players = tuple(Player(i, (100-i)/100) for i in range(1,10+1))
    num_trials = 1000
    
    # Run the simulation with you (99% correct) starting
    sb = Spelling_Bee(players)
    results = sb.run_trials(num_trials)
    plot_data_x, plot_data_y = zip(*[(p[0].name, p[1]/num_trials) for p in results.items()])
    p1 = pyplot.plot(plot_data_x, plot_data_y, 'bo')
    pyplot.xlabel('Probability of Winning')
    pyplot.ylabel('Player')
    pyplot.show()

    # Run the simulation with you (99% correct) last
    players_rev = tuple(reversed(players))
    sb = Spelling_Bee(players_rev)
    results = sb.run_trials(num_trials)
    plot_data_x, plot_data_y = zip(*[(p[0].name, p[1]/num_trials) for p in results.items()])
    p1 = pyplot.plot(plot_data_x, plot_data_y, 'bo')
    pyplot.xlabel('Probability of Winning')
    pyplot.ylabel('Player')
    pyplot.show()
    
