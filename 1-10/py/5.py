'''
Smallest multiple
'''
import math

def factorization(n):
  assert n >= 2
  factor = [0] * n
  for k in range(1, len(factor)):
    while n % (k+1) == 0:
      factor[k] = factor[k] + 1
      n = n / (k+1)
  return factor
    
def compute():
  largest_factor = [0] * 20
  for i in range(2,21):
    temp_factor = factorization(i)
    for idx, v in enumerate(temp_factor):
      if largest_factor[idx] < v:
        largest_factor[idx] = v
  return largest_factor
  
def combine(factor):
  ret = 1
  for idx, v in enumerate(factor):
    ret = ret * (idx + 1)**v
  return ret
      
if __name__ == '__main__':
  print(combine(compute()))
      
  
  
