import sys, textwrap

def prime_factors(num):
    factors = []
    for i in range(1,num + 1):
        if not(num % i):
            factors.append(i)
    factors.remove(num)
    return factors    

with open(sys.argv[1]) as f:
    ranges = f.read().split(",")
    ranges = [item.split("-") for item in ranges]

def part1():
    repeat_sum = 0
    for item in ranges:
        for i in range(int(item[0]),int(item[1])+1):
            if not(len(str(i)) % 2):
                if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
                    repeat_sum += i
    return repeat_sum

def part2():
    repeat_sum = 0
    for item in ranges:
         for i in range(int(item[0]),int(item[1])+1):
             # Only need to check factor strings
             factors = prime_factors(len(str(i)))
             for factor in factors:
                 substrings = textwrap.wrap(str(i), factor)
                 if len(set(substrings)) == 1:
                     repeat_sum += i
                     break
    return repeat_sum

print(part2())
