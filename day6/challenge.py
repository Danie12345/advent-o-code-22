with open('day6/device.txt', 'r') as device:
  posmarker, posmsg = 1, 1
  rngemrkr, rngemsg = 4, 14
  signal = str(device.read())
  def read_input_w_step(step = 1, iter = [], rnge = 1):
    cnt = -step
    for _ in range(len(iter)//step):
      cnt += step
      yield iter[cnt:cnt+rnge], cnt
  for buffer, i in read_input_w_step(iter=signal, rnge=rngemrkr):
    if len(set(buffer)) == rngemrkr:
      posmarker = i + rngemrkr
      break
  for buffer, i in read_input_w_step(iter=signal, rnge=rngemsg):
    if len(set(buffer)) == rngemsg:
      posmsg = i + rngemsg
      break
  print (posmarker)
  print (posmsg)
device.close()