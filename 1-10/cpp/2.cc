#include <iostream>

int main() {
  int prev = 0, cur = 1, next = 2;
  int sum = 0;

  while (cur <= 4'00'0000) {
    if (cur % 2 == 0) 
      sum += cur;
    prev = cur, cur = next;
    next = prev + cur;
  }

  std::cout << sum << "\n";
}

void l() {
  int sum = 0;
  for (int fibo1 = 1, fibo2 = 2; fibo2 <= 4000000;) {
    if (fibo2 % 2 == 0)
      sum += fibo2;
    fibo2 += fibo1;
    fibo1 = fibo2 - fibo1;
  }
  std::cout << sum << "\n";
}
