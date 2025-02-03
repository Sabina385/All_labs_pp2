import itertools

def permutations(some):
  for p in itertools.permutations(some):
    print("".join(p))

k = input("soz: ")
permutations(k)