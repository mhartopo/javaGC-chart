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
titles = ["GC Latency - Heap Size 512 MB","GC Latency - Heap Size 768 MB","GC Latency - Heap Size 1024 MB"]
i = 1
j = 0
while (i <= 9 ) :
  fdir = "log/"
  latsPar = spl.latlog_sorted(fdir + "log" + str(i) + ".txt")
  t = np.arange(0.1, 150.0, 0.001)
  cdf_res = cdf_arr(latsPar, t)
  
  i+=1
  latsg1 = spl.latlog_sorted(fdir + "log" + str(i) + ".txt")
  cdfg1 = cdf_arr(latsg1, t)

  i += 1
  latscms = spl.latlog_sorted(fdir + "log" + str(i) + ".txt")
  cdfcms = cdf_arr(latscms, t)

  line_par, = plt.plot(t, cdf_res, label='Line Par')
  line_g1, = plt.plot(t, cdfg1, label='Line G1')
  line_cms, = plt.plot(t, cdfcms, label='Line Cms')
  plt.legend([line_par, line_g1, line_cms], ['Parallel', 'G1', 'CMS'])
 
  plt.xlabel('latency time (ms)')
  plt.ylabel('CDF')
  print "save chart : " + titles[j] + ".jpg"
  plt.title(titles[j])
  plt.savefig(titles[j])
  plt.show()
  i += 1
  j += 1
  plt.clf()
print "done"
