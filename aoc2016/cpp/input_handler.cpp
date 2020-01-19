#include <string>
#include <climits>

std::string delPhrase(std::string line, std::string phrase)
{
	unsigned long index = line.find(phrase);
	if (index < ULONG_MAX)
	{
		std::string new_string = line.substr(0, index);
		new_string = new_string + line.substr(index + phrase.length(), -1);
		return new_string;
	}
	return line;
}

std::string clearPhrase(std::string line, std::string phrase)
{
	unsigned long index = line.find(phrase);
	if (index == ULONG_MAX)
	{
		return line;
	}

	std::string new_string = line;

	while (index < ULONG_MAX)
	{
		new_string = delPhrase(new_string, phrase);
		index = new_string.find(phrase);
	}

	return new_string;
}

unsigned int countPhrase(std::string line, std::string phrase)
{
	if (line.length() < phrase.length())
	{
		return 0;
	}

	unsigned int count = 0;
	unsigned long index = 0;

	if (line.find(phrase) == 0)
	{
		count++;
	}


	while (line.substr(index + phrase.length(), -1).find(phrase) < ULONG_MAX)
	{
		index = index + phrase.length() + line.substr(index + phrase.length(), -1).find(phrase);
		count++;
	}
	return count;
}

std::string* separateByPhrase(std::string line, std::string phrase)
{
	if (line.length() == 0)
	{
		return NULL;
	}

	unsigned int cell_count = countPhrase(line, phrase);

	std::string new_string = (std::string*) malloc(sizeof(std::string) * (cell_count + 1));

	unsigned long index = 0;
	unsigned long cutoff = 0;
	int count = 0;
	while (line.substr(index, -1).find(phrase) < ULONG_MAX)
	{
		cuttoff = line.substr(index, -1).find(phrase);
		new_string[count] = line.substr(index, cutoff);
		index = index + phrase.length() + line.find(phrase);

	}

}