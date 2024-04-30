#include <iostream>
#include <string>
#include <vector>
#include <array>

#define size_arr 140

struct number {
    int start_pos;
    int end_pos;
};

std::vector<number> parse_str(std::string& input);

int main() {
    std::array<std::string, size_arr> inputs;
    //std::regex pattern(R"(\d+)");

    for(int i = 0; i < 140; i++) {
        std::getline(std::cin, inputs[i]);
    } 
    for(int i = 0; i < 1; i++) {

        //std::regex_search(inputs[i], match, pattern);
        //std::cout << "Length: " << match.size() << std::endl;
        /*
        std::cout << "String: " << inputs[0] << std::endl;
        while(std::regex_search(input, match, pattern)) {
            std::cout << "e" << std::endl;
            std::cout << match.position() + counter << match.str() << "\n";
            counter += match.position() + match.length();
            input = match.suffix();
        }
        */
    }
    std::string foo = "42..13..123..0";
    std::vector<number> matches = parse_str(foo);
    for(number num : matches) {
        std::cout << num.start_pos << " : " <<  num.end_pos << std::endl;
    }
}

std::vector<number> parse_str(std::string& input) {
    int pos = -1;
    std::vector<number> matches;
    for(int i = 0; i < input.length(); i++) {
        if (input[i] >= '0' && input[i] <= '9'){
            if (pos == -1) {
                pos = i;
            }
        } else {
            if (pos != -1) {
                number num = {
                    pos,
                    pos+i-1
                };
                matches.push_back(num);
                pos = -1;
            }
        }
    }
    if (pos != -1) {
        number num = {
            pos,
            (int) input.length() - 1
        };
        matches.push_back(num);
    }
    return matches; 
}