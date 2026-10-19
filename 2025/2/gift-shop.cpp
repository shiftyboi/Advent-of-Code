#include <unordered_map>
#include <vector>


class FactorFinder {
    public:

        std::vector<int> findFactors(int value){

            if (lengthFactors.find(value) != lengthFactors.end()) {
                return lengthFactors[value]
            } else {
                for (int i=0; i<value; i++) {

                    std::vector<int> factors;
                    if (!(value % i)) {
                        factors.push_back(i)
                    }
                lengthFactors[i] = factors;
                return factors;
                }
            }
        }

    private:
        std::unordered_map<int, std::vector<int>> lengthFactors;
};
