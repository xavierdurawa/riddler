from scipy.stats import expon

rate = 1 # number of comments in 3 days
time_elapse = 2.6 # amount of time we care about


def recursive_sample_tree(sample_distribution, rate, time_elapse):
    total = 0
    time_remaining = time_elapse
    while time_remaining > 0:
        time_until_next_comment = sample_distribution.rvs(scale=(1/rate))
        time_remaining = time_elapse - time_until_next_comment
        if time_remaining > 0:
            total += 1 + recursive_sample_tree(sample_distribution, rate, time_remaining)
    return total

print(recursive_sample_tree(expon, rate, time_elapse))