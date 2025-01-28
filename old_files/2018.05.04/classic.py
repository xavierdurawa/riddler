# Generates the function that relates the inital pile of coconuts
# to the pile once each pirate has stolen from it.

def func(m, n, give):
    tot = m
    for i in range(n):
        tot *= n/(n-1)
        tot += give
    return tot

pirates = 7
give_to_monkey = 1

# Check through a huge number of values
# because I don't know how to find it a better way.

for i in range(100000000):
    ans = func(i,pirates,give_to_monkey)
    if ans.is_integer() and i % 7 == 0:
        print(ans)
