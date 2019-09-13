#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profit = prices[1]-prices[0]
  strike_price = prices[0]
  print(profit)
  if len(prices) <= 1: 
    profit = 0
    print(profit)
  else: 
    profit = prices[1]-prices[0]
    print(profit)
    for i in range(1, len(prices)):
      if prices[i]-strike_price > profit: 
        profit = prices[i]-strike_price 
      if prices[i] < strike_price: 
        strike_price = prices[i] 
      
  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))