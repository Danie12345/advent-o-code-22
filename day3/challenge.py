with open('day3/rucksacks.txt', 'r') as sacks:
  repeatedTotal = 0
  badgesTotal = 0

  def read_lines_w_step(step, lines):
    cache = [line.strip() for line in lines.readlines()]
    cnt = -step
    for _ in range(len(cache)//step):
      cnt += step
      yield cache[cnt:cnt+step]
  
  intersection = lambda A, B: [i for i in A if i in B]
  calc_value = lambda char: ord(char.swapcase()) - 64 - 6*(char.isupper())

  def read3lines(sacks):
    total = 0
    for sack in sacks:
      sack = sack.strip()
      size = len(sack)
      cmprta = sack[0:size//2]
      cmprtA = sack[size//2:]
      char = intersection(cmprta, cmprtA)[0]
      total += calc_value(char)
    return total
  
  for sackGroup in read_lines_w_step(3, sacks):
    repeatedTotal += read3lines(sackGroup)
    a, b, c = sackGroup
    badgesTotal += calc_value(intersection(intersection(a, b), c)[0])

  print (repeatedTotal)
  print (badgesTotal)

sacks.close()