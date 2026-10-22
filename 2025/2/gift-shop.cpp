#include <array>
#include <fstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <iostream>
#include "cleanData.cpp"



class FactorFinder {
    public:

        std::vector<int> findFactors(int value){

            if (lengthFactors.find(value) != lengthFactors.end()) {
                return lengthFactors[value];
            } else {
                for (int i=0; i<value; i++) {

                    std::vector<int> factors;
                    if (!(value % i)) {
                        factors.push_back(i);
                    };
                lengthFactors[i] = factors;
                return factors;
                }
            }
            return std::vector<int>(-1);
        }

    private:
        std::unordered_map<int, std::vector<int>> lengthFactors;
};

class Solution {
    public:

        Solution(FactorFinder f, std::vector<std::array<int, 2>> r) {
            factorFinder = f;
            ranges = r;
        }

        int part2() {
            int repeatSum = 0;
            return 0;

        }

    private:
        FactorFinder factorFinder;
        std::vector<std::array<int, 2>> ranges;
};

int main(int argc, char *argv[]){

    std::string fileLine;
    std::ifstream inputFile(argv[1]);
    std::getline(inputFile, fileLine);
    std::vector<std::vector<long long>> ranges = cleanData(fileLine);
    std::cout << "Done";
    }
