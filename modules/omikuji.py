import random

def omikuji(fortunes):

  r = random.randint(0,len(fortunes) -1)
  
  return fortunes[r]


if __name__ == "__main__":
  print(omikuji())
