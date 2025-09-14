#include <iostream>

int main() {
  int N, C, P;
  std::cin >> N >> C >> P;
  if (N <= C * P) std::cout << "yes" << std::endl;
  else std::cout << "no" << std::endl;
}
