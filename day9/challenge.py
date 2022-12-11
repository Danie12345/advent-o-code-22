class Knot:
  def __init__(self):
    self.coords, self.stepped = [0, 0], set()
    self.parent, self.child = None, None

  def move_attempt(self):
    px, py, sx, sy = *self.parent.coords, *self.coords
    d = abs(px - sx) + abs(py - sy)
    self.coords = sx + ((sx < px) + ((sx < px)-1))*((py == sy or d!=2))*(d>1), sy + ((sy < py) + ((sy < py)-1))*((px == sx or d!=2))*(d>1)
    self.stepped.add(f'{self.coords[0]},{self.coords[1]}')
    if self.child is not None: self.child.move_attempt()

with open('day9/movements.txt', 'r') as moves:
  coordscalculator, knotqty = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}, 10
  body = head = Knot()
  for i in range(knotqty - 1):
    body.child = Knot()
    body.child.parent = body
    body = body.child
    if i == 0: firstknot = body
    elif i == knotqty - 2: tail = body
  for move in moves.readlines():
    direction, steps = move.strip().split(' ')
    dx, dy = coordscalculator[direction]
    for step in range(int(steps)):
      head.coords = head.coords[0] + dx, head.coords[1] + dy
      head.child.move_attempt()
  print (len(firstknot.stepped))
  print (len(tail.stepped))
moves.close()