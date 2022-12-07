with open('day7/filesystem.txt', 'r') as commands:
  newdir = lambda name: {'name': name, 'subdirs': {}, 'files': {}, 'accsize': 0, 'parent': None}
  dir = sys = newdir('/')
  alldirs = []
  def bubblesize(dir, size):
    dir['accsize'] += size
    if dir['parent'] != None:
      bubblesize(dir['parent'], size)
  def exec(cmd, dir):
    global sys
    if '$ cd' in cmd:
      if '/' in cmd:
        return sys
      elif '..' in cmd:
        if dir['parent'] == None:
          return sys
        return dir['parent']
      subdir = cmd.split(' ')[-1]
      if subdir in dir['subdirs'].keys():
        return dir['subdirs'][subdir]
    elif 'dir ' in cmd:
      dirname = cmd.split(' ')[-1]
      subdir = newdir(dirname)
      alldirs.append(subdir)
      subdir['parent'] = dir
      dir['subdirs'][dirname] = subdir
    elif '$ ls' not in cmd:
      size, file = cmd.split(' ')
      bubblesize(dir, int(size))
      dir['files'][file] = int(size)
    return dir
  for command in commands.readlines():
    dir = exec(command.strip(), dir)
  print (sum([dir['accsize'] if dir['accsize'] <= 100_000 else 0 for dir in alldirs]))
  print (min([dir['accsize'] if 70_000_000 - sys['accsize'] + dir['accsize'] >= 30_000_000 else sys['accsize'] for dir in alldirs]))
commands.close()