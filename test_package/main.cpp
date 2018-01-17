#include <string>
#include <sstream>
#include <iostream>
<<<<<<< HEAD
#include "yaml.h"
=======
#include "yaml-cpp/yaml.h"
>>>>>>> testing/0.3.0

int main() {
		std::string input =
						"- eggs\n"
						"- bread\n"
						"- milk";

		std::stringstream stream(input);
		YAML::Parser parser(stream);
		YAML::Node doc;
		parser.GetNextDocument(doc);
		for (int i = 0; i < 3; ++i) {
			  std::string out;
				doc[i] >> out;
				std::cout << out << '\n';
		}

		return 0;
<<<<<<< HEAD
}
=======
}
>>>>>>> testing/0.3.0
