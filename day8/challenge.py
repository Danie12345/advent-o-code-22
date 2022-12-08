with open('day8/treegrid.txt', 'r') as trees:
  grid, scores = [], []
  for treeline in trees.readlines():
    grid.append([int(tree) for tree in treeline.strip()])
  visibletrees = 2*len(grid) + 2*len(grid[0]) - 4
  tgrid = [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]
  grid_slices = lambda x, y: (grid[y][x+1:], grid[y][:x], tgrid[x][y+1:], tgrid[x][:y])
  def calc_score(tree, arr, score = 0):
    for t in arr:
      score += 1
      if t >= tree: break
    return score
  def check_edgescore(tree, x, y, edgescore = 'edge'):
    r, l, d, u = grid_slices(x, y)
    return (tree > max(r+[0]) or tree > max(l+[0]) or tree > max(d+[0]) or tree > max(u+[0])) if edgescore == 'edge' else (calc_score(tree, r) * calc_score(tree, l[::-1]) * calc_score(tree, d) * calc_score(tree, u[::-1]))
  for y, row in enumerate(grid):
    for x, tree in enumerate(row):
      visibletrees += check_edgescore(int(tree), x, y) * ((x > 0 and x < len(grid[0])-1) and (y > 0 and y < len(grid)-1))
      scores.append(check_edgescore(int(tree), x, y, 'score'))
  print (visibletrees)
  print (max(scores))
trees.close()