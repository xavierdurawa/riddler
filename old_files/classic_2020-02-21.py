import random 
import multiprocessing

class GameSimulation(object):

    def __init__(self, num_coins, prob_coins):
        self.num_coins = num_coins
        self.prob_coins = prob_coins
        self.winnings = 0
    
    def run_round(self, which_coin):
        if random.random() < self.prob_coins[which_coin - 1]:
            self.winnings += which_coin
    
    def run_game(self, num_rounds):
        for i in range(num_rounds):
            # Code to figure out which coin to pick
            self.run_round()

    

