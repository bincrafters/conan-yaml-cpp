#include <string>
#include <iostream>
#include "yaml-cpp/yaml.h"

int main() {
	  YAML::Node node = YAML::Node("Hello, World!");
		if (node.IsScalar()) {
				std::cout << node.as<std::string>() << std::endl;
		}
		return 0;
}
