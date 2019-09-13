#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  possible_plays = [['rock'], ['paper'], ['scissors']]
  output_array = []
  if n > 0:
    print("n", n)
    for item in range(0, n):
      print("item", item)
      output_array.append(possible_plays)
      rock_paper_scissors(n-1)
  print(output_array)
  return output_array 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')