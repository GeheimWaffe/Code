# Testing inline parameters
import sys

def mainMethod():
  print('mainMethod')

  args = sys.argv

  print('argument 1 : {}'.format(args[0]))
  print('argument 2 : {}'.format(args[1]))
  print('argument 3 : {}'.format(args[2]))

mainMethod()
