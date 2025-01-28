import random
from matplotlib import pyplot as plt
import operator
from multiprocessing import cpu_count, Pool

class Gift_Cards(object):

    def __init__(self, num_cards = 2, num_drinks_on_card = 50):
        self.num_cards = num_cards
        self.num_drinks_on_card = num_drinks_on_card

    def use_cards(self):
        """Run a simulation of randomly using the gift cards
        
        Arguments: (none)
        Return:
        left_on_cards: dictionary of number of drinks left on each card
        """
        random.seed()
        left_on_cards = {str(i+1):50 for i in range(self.num_cards)}
        any_declined = False
        while not any_declined:
            c = str(random.randint(1, self.num_cards))
            left_on_cards[c] -= 1
            if left_on_cards[c] == -1:
                any_declined = True
            else:
                continue
        return left_on_cards
    
    def run_2_cards_trials(self, num_trials):
        """Runs trials for the case with 2 cards

        Arguments:
        num_trails: number of trials to be run
        Return:
        avg_drinks_left: average num drinks remaining on other card
        """       
        assert(self.num_cards == 2)
        drinks_left = []
        for i in range(num_trials):
            drinks_left.append(max(self.use_cards().items(), key=operator.itemgetter(1))[1])
        return (sum(drinks_left)/num_trials, drinks_left)

    def parallel_2_cards_trials(self, num_trials):
        """Runs trials for the case with 2 cards in parallel

        Arguments:
        num_trails: number of trials to be run
        Return:
        avg_drinks_left: average num drinks remaining on other card
        """       
        assert(self.num_cards == 2)
        pool = Pool(cpu_count())

        results = [pool.apply_async(self.use_cards) for _ in range(num_trials)]
        drinks_left = [max(r.get().items(), key=operator.itemgetter(1))[1] for r in results]
        return (sum(drinks_left)/num_trials, drinks_left)

if __name__ == "__main__":
    num_trials = 1000000
    g = Gift_Cards(2, 50)
    avg_drinks, dist_drink = g.parallel_2_cards_trials(num_trials)

    print("{0}% chance that the other card still has free drinks".format((1 - dist_drink.count(0) / num_trials)*100))
    print("Average of {0} free drinks remaining on the other card".format(avg_drinks))
    plt.hist(dist_drink, bins=range(40))
    plt.show()
        
        