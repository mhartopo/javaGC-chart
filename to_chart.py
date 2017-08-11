import numpy as np
import matplotlib.pyplot as plt
import split as spl


def cdf(arr, value):
  count = 0
  total = len(arr)
  for num in arr:
    if np.any(num <= value):
      count += 1
  return count/float(total)

def cdf_arr(arr, values):
  res = []
  start = 0
  for val in values :
    cdf_val = cdf_tes(arr, val, start)
    start =  cdf_val[1]
    res.append(cdf_val[0])
  return res

def cdf_tes(arr, val, start):
  count = 0
  total = len(arr)
  i = start
  found = False
  cnt = start
  while (i < total and found == False) :
    found = arr[i] > val
    if found == False :
      cnt += 1
    i += 1
  ret = []
  ret.append(cnt/float(total))
  ret.append(i-1)
  return ret

#main
'''
print "Enter file name : "
fname = raw_input()
print "Enter Chart Title : "
title = raw_input()
'''
i = 1
while (i <= 9 ) :
  fname = "log" + str(i)
  fdir = "log/"
  lats = spl.latlog_sorted(fdir + fname + ".txt")
  t = np.arange(0.1, 150.0, 0.001)
  cdf_res = cdf_arr(lats, t)
  plt.plot(t, cdf_res)
  plt.xlabel('latency time (ms)')
  plt.ylabel('CDF')
  #plt.title(title)
  chartName  = "chart/" + fname + "chart" + ".png" 
  print "save chart : " + chartName
  plt.savefig(chartName)
  i += 1
  plt.clf()
print "done"
#plt.show()
