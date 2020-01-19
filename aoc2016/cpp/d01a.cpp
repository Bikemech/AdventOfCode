#include <climits>
#include <iostream>
#include <string>
#include "input_handler.cpp"

int main ()
{
	std::string a = "but different to computers. Luckily, zero-width spaces are prohibited in";
	std::string b = clearPhrase(a, " ");

	std::cout << countPhrase(a, " ") << std::endl;

	return 0;
}