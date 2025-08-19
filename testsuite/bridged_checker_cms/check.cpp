#include <fstream>
#include <iostream>
#include <string>

int main(int argc, char **argv) {
  std::ifstream judge_stream(argv[2]), output_stream(argv[3]),
      input_stream(argv[1]);
  std::string input_string, judge_string;
  int i;
  std::getline(input_stream, input_string);
  if (input_string != "This is the input file.") {
    return -1;
  }
  std::getline(judge_stream, judge_string);
  if (judge_string != "This is the judge file.") {
    return -1;
  }
  output_stream >> i;
  if (1 <= i && i <= 10) {
    std::cout << 1.0 * i / 10;
    return 0;
  } else {
    std::cout << 0;
    return 0;
  }
}
