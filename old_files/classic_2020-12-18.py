phi = (1 + 5**0.5)/2

def game_check(n, m, p1_turn=True):
    if m-n <= 0:
        return p1_turn
    else:
        return game_check(m-n, n, not p1_turn)

results = []
for i in range(1,10000):
    num1 = int(i*phi)
    for j in reversed(range(i,2*i)):
        if game_check(i, j):
            num2 = j
            break
    results.append(num1 == num2)

if all(results):
    print('all good')
else:
    print('errors somewhere')        
