def min_divisible_size(k):
    s = list(range(1,2*k+1))
    n = max(s)
    group_size = n*(n+1)/(2*k)
    min_set = n
    while n <= group_size:
        if group_size.is_integer():
            min_set = n
        s.pop(-1)
        n = max(s)
        group_size = n*(n+1)/(2*k)
    return min_set


for i in range(2,10000):
    # print("{}: {} vs {}".format(i, min_divisible_size(i), 2*i-1))
    if min_divisible_size(i)==2*i-1:
        pass
    else:
        print("{}: {} vs {}".format(i, min_divisible_size(i), 2*i-1))