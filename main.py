#args allows me to use as many arguments as possible, that I want

def sum(*args):
  total = 0
  for arg in args:
    total += arg
  return total
  
print(sum(2,3,44,33,3,33,3,3,2,23,2,3,42,34,234))

#kwargs mean using key values (limitless)