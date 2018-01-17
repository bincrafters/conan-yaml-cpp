#include <string>
#include <sstream>
#include <iostream>
#include "yaml.h"

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
}