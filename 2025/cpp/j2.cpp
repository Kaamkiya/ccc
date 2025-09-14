#include <iostream>

int main() {
  int D, E, Q;
  char op;
  std::cin >> D >> E;

  for (int i = 0; i < E; i++) {
    std::cin >> op >> Q;
    if (op == '+') D += Q;
    else D -= Q;
  }

  std::cout << D << std::endl;
}
