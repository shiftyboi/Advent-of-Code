#include <sstream>
#include <string>
#include <vector>

std::vector<std::vector<long long>> cleanData(std::string text) {

    std::stringstream sstext(text);
    std::string tempRange;

    std::vector<std::vector<long long>> out;

    while(std::getline(sstext, tempRange, ',')) {

        std::stringstream ssrange(tempRange);
        std::string tempValue;
        std::vector<long long> rangeVect;

        while (std::getline(ssrange, tempValue, '-')) {

            long long tempLong = std::stol(tempValue);
            rangeVect.push_back(tempLong);

        }

        out.push_back(rangeVect);


    }

    return out;
}
