with open('day4/cleaningpairs.txt', 'r') as pairs:
  contained = 0
  intersected = 1000
  contains = lambda a, b: int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1])
  intersects = lambda a, b: int(a[0]) > int(b[1]) or int(a[1]) < int(b[0])
  for pair in pairs:
    a, b = [x.split('-') for x in pair.strip().split(',')]
    contained += (1 + contains(a, b) + contains(b, a))//2
    intersected -= (1 + intersects(a, b) + intersects(b, a))//2
  print (contained)
  print (intersected)
pairs.close()