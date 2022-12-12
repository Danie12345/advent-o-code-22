from copy import deepcopy
from math import prod
with open('day11/monkeys.txt', 'r') as monkeys:
  monki = lambda id, items, op, div, t, f: {'id': id, 'items': items, 'op': op,  'div': div, 't': t, 'f': f, 'held': 0}
  monkis, recent = {}, []
  for line in monkeys.readlines():
    line = line.strip()
    if 'Monkey ' in line:
      id = int(line.split(' ')[1][:-1])
      recent.append(id)
    elif 'Starting items:' in line:
      items = eval('['+line.split(': ')[1]+']')
      recent.append(items)
    elif 'Operation:' in line:
      op = line.split('= ')[1]
      recent.append(op)
    elif 'Test: ' in line:
      div = int(line.split('by ')[1])
      recent.append(div)
    elif 'true: ' in line:
      t = int(line.split('monkey ')[1])
      recent.append(t)
    elif 'false: ' in line:
      f = int(line.split('monkey ')[1])
      recent.append(f)
    else:
      monkis[recent[0]] = monki(*recent)
      recent = []
  monkis10000 = deepcopy(monkis)
  def keepaway(rounds, monkis, unworrier = 1):
    if unworrier == 1:
      unworrier = prod([monke['div'] for monke in monkis.values()])
    for _ in range(rounds):
      for monke in monkis.values():
        for i in range(len(monke['items'])):
          worry = monke['items'][i]
          monke['held'] += 1
          worry = eval(monke['op'].replace('old', str(worry)))
          if unworrier == 3: worry //= unworrier
          else: worry %= unworrier
          monkis[monke['t' if worry%monke['div'] == 0 else 'f']]['items'].append(worry)
        monke['items'] = []
    heldworries = []
    for monke in monkis.values():
      heldworries.append(monke['held'])
    worries = sorted(heldworries)[-2:]
    return worries[0] * worries[1]
  print (keepaway(20, monkis, 3))
  print (keepaway(10000, monkis10000))
monkeys.close()