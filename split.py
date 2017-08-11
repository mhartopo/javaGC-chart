import numpy as np
import matplotlib.pyplot as plt

def split_log(log):
  arr = log.split()
  length = len(arr)
  if arr[length - 1] == "secs]" :
    return arr[length - 2]
  else :
    return "nothing"

#latency in millisecon
def latency_log(fileName):
  f = open(fileName,"r")
  times = []
  for line in f:
    time = split_log(line)
    if time != "nothing" :
      time = time.replace("real=","")
      times.append(float(time.replace(",", "."))*1000)
  return times
def latlog_sorted(fileName):
  lats = latency_log(fileName)
  lats.sort()
  return lats