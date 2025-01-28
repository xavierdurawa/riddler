import random
from matplotlib import pyplot as plt
import multiprocessing as mp

class Dynamic_Dice(object):
    
    def __init__(self, num_faces):
        self.num_faces = num_faces
        self.faces = list(range(1,num_faces+1))
    
    def run_round(self):
        new_faces = []
        for i in range(self.num_faces):
            new_faces.append(random.choice(self.faces))
        self.faces = new_faces
    
    def run_game(self):
        num_rounds = 0
        while len(set(self.faces)) != 1:
            self.run_round()
            num_rounds += 1
        return num_rounds

num_simulations = 1000000
results = []
for i in range(num_simulations):
    d = Dynamic_Dice(6)
    results.append( d.run_game() )

print(sum(results)/len(results))
plt.hist(results)
plt.show()