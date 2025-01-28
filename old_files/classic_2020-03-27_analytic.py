import math

def choose(n,m):
    f = math.factorial
    return f(n) / (f(n-m)*f(m))

P = []
num_sides_die = 6
# inital probablilities
P1 = []
for i in range(1,num_sides_die+1):
    c = choose(num_sides_die,i)
    y = (1/num_sides_die)**i
    n = ((num_sides_die-1)/num_sides_die)**(num_sides_die-i)
    P1.append( c*y*n )
P.append(P1)

# calculate subsequent probablilities
num_layers = 100
for i in range(1,num_layers+1):
    P_temp = []
    for j in range(1,num_sides_die+1):
        P_temp_temp = []
        c = choose(num_sides_die,j)
        for k in range(1,num_sides_die):
            p = P[i-1][k-1]
            y = (k/num_sides_die)**j
            n = ((num_sides_die-k)/num_sides_die)**(num_sides_die-j) 
            P_temp_temp.append( p * c * y * n )
        P_temp.append(sum(P_temp_temp))
    P.append(P_temp)

print(sum([(i+1) * P[i][5] for i in range(len(P))]))