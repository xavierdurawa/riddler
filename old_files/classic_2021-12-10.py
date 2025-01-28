def calculation(percentages, round_cutoffs):
    """calculates the probability of your team winning the game described above
    
    Parameters:
        percentages (list): likehood your player wins a given game 
        round_cutoffs (list of ints): number of games each set of competitors must win before starting the next round

    Returns:
        p
    """

    from decimal import Decimal

    def which_round(n, m):
        i = 0
        while True:
            if n < round_cutoffs[i] and m < round_cutoffs[i]:
                return i
            else:
                i += 1

    import numpy as np

    total_rounds = round_cutoffs[-1]

    probabilities = np.zeros([total_rounds, total_rounds])
    
    # Set boundary conditions
    probabilities[-1, :] = Decimal(1)

    for i in reversed(range(0, total_rounds-1)):
        for j in reversed(range(0, total_rounds-1)):
            round_num = which_round(i+1,j+1) 
            p = percentages[round_num]
            probabilities[i, j] = p * probabilities[i+1, j] + (1-p) * probabilities[i, j+1]
    
    return probabilities[0][0]

perc = [.25, .5, .75]
rounds = [15, 30, 45]
print(calculation(perc, rounds))