import math
import matplotlib.pyplot as plt

def choose(n, m):
  f = math.factorial
  return f(n)/(f(n-m)*f(m))

def pAllSpy(n, s, r):
  if r < s:
    return 0
  else:
    return choose(r,s)/choose(n,s)

def estimate_num_trips(n, s, frac):
  tot = 0
  n_temp = n
  r = int(n*frac)
  while n_temp > s/frac:
    tot += (n_temp-r)/pAllSpy(n_temp,s,r)
    n_temp = n_temp - r
    r = int(n_temp*frac)
  return tot

n=1024
s=17

eVals = []
for r in range(1,10):
  frac = r/10
  eVals.append(estimate_num_trips(n, s, frac))

# pVals = []
# for r in range(17,n):
#   pVals.append((n-r)/pAllSpy(n, s, r))

# q=2**5
# r = int(n*(q-1)/q)
# print(n-r)
plt.plot(eVals)
plt.show()