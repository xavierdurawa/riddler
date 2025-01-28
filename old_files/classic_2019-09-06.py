import math

def choose(n,m):
    f = math.factorial
    return f(m)/(f(n)*f(m-n))

def calc_prob_win_game(prob_win_point):
    # 4 points needed to win a game
    # opponenet can win 0, 1, 2, or 3 points
    ans = 0
    for i in range(0,3):
        ans += prob_win_game**4 * (1-prob_win_game)**i * choose(i,3+i)
    return ans

def calc_prob_win_set(prob_win_game):
    # 6 games needed to win set 