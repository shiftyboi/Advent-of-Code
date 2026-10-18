import sys, textwrap

def factors_of(num):
    
    factors = []
    for i in range(1,num + 1):
        if not(num % i):
            factors.append(i)
    factors.remove(num)
    return factors    

class Factors_of:
    def __init__(self):
        self.prev = {}
    
    def find_factors(self, num):
        if num in self.prev.keys():
            return self.prev[num]
        
        factors = []
        for i in range(1,num + 1):
            if not(num % i):
                factors.append(i)
        factors.remove(num)
        self.prev[num] = factors
        return factors


with open(sys.argv[1]) as f:
    ranges = f.read().split(",")
    ranges = [item.split("-") for item in ranges]

class Solution:
    def __init__(self, ranges, factor_finder : Factors_of):
        self.ranges = ranges
        self.factor_finder = factor_finder

    def part1(self):
        repeat_sum = 0
        for item in self.ranges:
            for i in range(int(item[0]),int(item[1])+1):
                if not(len(str(i)) % 2):
                    if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
                        repeat_sum += i
        return repeat_sum

    def part2(self):
        repeat_sum = 0
        for item in self.ranges:
            for i in range(int(item[0]),int(item[1])+1):
                # Only need to check factor strings
                factors = self.factor_finder.find_factors(len(str(i)))
                for factor in factors:
                    substrings = textwrap.wrap(str(i), factor)
                    if len(set(substrings)) == 1:
                        repeat_sum += i
                        break
        return repeat_sum

factor_finder = Factors_of()
solution = Solution(ranges, factor_finder)

print(solution.part2())