#include <string>
#include <iostream>
#include "yaml-cpp/yaml.h"

int main() {
    YAML::Node primes = YAML::Load("[2, 3, 5, 7, 11]");
		std::cout << "Size: " << primes.size() << '\n';
		return 0;
}
