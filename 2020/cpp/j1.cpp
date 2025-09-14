#include <iostream>

int main() {
  int S, M, L;
  std::cin >> S >> M >> L;
  if (S + 2*M + 3*L > 9) std::cout << "happy" << std::endl;
  else std::cout << "sad" << std::endl;
}
