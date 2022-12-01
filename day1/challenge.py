import numpy as np

with open('day1/calories.txt', 'r') as txtcalories:
  calories = f'[{txtcalories.readlines()}]'
  calories = eval(calories.replace("\'", "").replace('n', "").replace("\\", '').replace(', , ', '], ['))
  sums = np.sort([sum(caloriegroup) for caloriegroup in calories], kind='mergesort')
  mostcalories = max(sums)
  print (mostcalories)
  print (mostcalories + sum(sums[-3:-1]))

txtcalories.close()