import random
import multiprocessing as mp

def generate_number():
    prev = random.randint(0,9)
    number = prev/10
    i = 2
    while True:
        d = random.randint(0,9)
        if d == 0: break
        elif d > prev: continue
        else:
            prev = d
            number += d/(10**i)
            i += 1
    return number


with mp.Pool(mp.cpu_count()) as pool:
    future_results = [pool.apply_async(generate_number) for i in range(10**6)]
    results = [f.get() for f in future_results]
    print(sum(results)/len(results))