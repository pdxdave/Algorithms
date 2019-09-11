#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
   # the number of ways to eat negative cookies
    if n < 0:
        return 0
    # the number of ways to eat 0 cookies. 
    # not eating them is a way I suspect. like deciding not to decide?
    elif n == 0:
        return 1
  
    count = ( eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache) )
    return count

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')