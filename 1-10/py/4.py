'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def is_palindromic(n):
  return n == palindrome(n)


def palindrome(n):
  tmp = 0
  while n > 0:
    tmp = tmp * 10 + n % 10
    n = n // 10
  return tmp


def compute():
  # 100 - 999
  largest_palindrome = 0
  for i in range(100,1000):
    for j in range(i, 1000):
      if is_palindromic(i*j) and i*j > largest_palindrome:
        largest_palindrome = i*j
  return largest_palindrome

if __name__ == '__main__':
  print(compute())
    