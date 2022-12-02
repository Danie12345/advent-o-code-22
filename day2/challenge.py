with open('day2/rockpaperscissorsstrats.txt', 'r') as guides:
  initialscore = 0
  realscore = 0
  draws = {'A': 1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
  for guide in guides.readlines():
    g = guide.strip().replace(' ', '')
    initialscore += draws[g[1]] + 3*((- draws[g[0]] + draws[g[1]] + 1)%3)
    realscore += (((draws[g[0]] + draws[g[1]])%3) + 1) + 3*(draws[g[1]] - 1)
  print (initialscore)
  print (realscore)

guides.close()