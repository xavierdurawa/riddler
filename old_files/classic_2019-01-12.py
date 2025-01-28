import math

base_num_str = '53013180176278773980288979275410970{0}139358547710066257652050346294484433323974747960297803292989236183040000000000'

for i in range(0, 10):
    num = int(base_num_str.format(i))

    factors = {}
    while True:
        doesnt_work = False
        n = 99
        while True:
            if n < 2:
                doesnt_work = True
                break
            elif num % n == 0:
                num /= n
                if n not in factors:
                    factors[n] = 1
                else:
                    factors[n] += 1
                break
            else:
                n -= 1
        
        print(num)
        if doesnt_work:
            print(int(base_num_str.format(i)))
            print("Number {} doesn't work".format(i))
            break
        elif num == 1:
            print('Possible solution found')
            print(factors)
            break
        else:
            continue
