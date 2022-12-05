from copy import deepcopy
with open('day5/crates.txt', 'r') as cratesfile:
  crates, moves = ''.join(cratesfile.readlines()).split(' 1   2   3   4   5   6   7   8   9 ')
  crates = crates.replace('[', '').replace(']', '').replace(5*' ', 3*' ').replace(7*' ', 5*' ').replace(9*' ', 7*' ').split('\n')[:-1]
  crates[0] = crates[0][:-2]
  crates = [[crates[y][x] if crates[y][x] != ' ' else '' for y in range(len(crates))] for x in range(len(crates[0]))]
  crates = [''.join(crates[r]).strip() for r in range(0, len(crates), 2)]
  crates9001 = deepcopy(crates)
  moves = moves.strip().split('\n')
  moves = [move.split('from') for move in moves]
  moves = [[int(move[0].replace('move ', '').strip()), *[int(m) - 1 for m in move[1].strip().split('to')]] for move in moves]
  for move in moves:
    crates[move[2]] = crates[move[1]][0:move[0]][::-1] + crates[move[2]]
    crates[move[1]] = crates[move[1]][move[0]:]
    crates9001[move[2]] = crates9001[move[1]][0:move[0]] + crates9001[move[2]]
    crates9001[move[1]] = crates9001[move[1]][move[0]:]
  tops = ''.join([crate[0] for crate in crates])
  tops9001 = ''.join([crate[0] for crate in crates9001])
  print (tops)
  print (tops9001)
cratesfile.close()