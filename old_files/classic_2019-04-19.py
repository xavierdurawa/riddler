import random
import math

def run_circle_simulation(num_points):
    theta = []
    for i in range(num_points):
        theta.append(random.random()*2*math.pi)
    max_theta = max(theta)
    min_theta = min(theta)

    # Check if max-min < pi
    if abs(max_theta - min_theta) < math.pi:
        return True
    else:
        return False
    
def run_simulations(num_point, num_trials):
    results = []
    for i in range(num_trials):
        results.append(run_circle_simulation(n))
    
    return results

if __name__ == "__main__":
    num_points = 10
    num_trials = 100000
    for n in range(1, num_points+1):
        results = run_simulations(n, num_trials)

        print("Probability with {0} points: {1}".format(n, sum(results)/len(results)))
