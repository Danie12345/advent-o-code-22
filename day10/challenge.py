with open('day10/instructions.txt', 'r') as instructions:
  addedcyclesums = 0
  nthcycle = 0
  x = 1
  row, col = 0, 0
  w, h = 40, 6
  screen = [[' ' for _w in range(w)] for _h in range(h)]
  sprite = lambda x: [x - 1, x, x + 1]
  for instruction in instructions.readlines():
    instruct, *cycles = instruction.strip().split(' ')
    cycleamts, timedcycled = {'noop': 1, 'addx': 2}, 0
    for _ in range(cycleamts[instruct]):
      col = nthcycle
      row += col%40 == 0
      Y, X = row-1, col%40
      if nthcycle%40 in sprite(x):
        screen[Y][X] = '#'
      nthcycle += 1
      if (nthcycle - 20)%40 == 0:
        addedcyclesums += x * nthcycle
      timedcycled += 1
      if timedcycled == 2 and instruct == 'addx':
        x += int(cycles[0])
  print (addedcyclesums)
  for row in screen:
    print (''.join(row))
instructions.close()