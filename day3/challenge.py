with open('day3/rucksacks.txt', 'r') as sacks:
  total = 0
  for sack in sacks.readlines():
    sack = sack.strip()
    size = len(sack)
    cmprta = sack[0:size//2]
    cmprtA = sack[size//2:]
    char = [i for i in cmprta if i in cmprtA][0]
    total += ord(char.swapcase()) - 64 - 6*(char.isupper())


  print (total)

sacks.close()