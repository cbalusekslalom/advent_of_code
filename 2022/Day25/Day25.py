str_map = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
int_map = {2:"2", 1:"1", 0:"0", -1:"-", -2:"="}


def converter(inString: str) -> int:
    sumVal = 0
    for ind, val in enumerate(inString[::-1]):
        sumVal += str_map[val] * 5**ind
    return sumVal


def power_sum(nth: int) -> int:
    return 2*sum([5**n for n in range(nth+1)])


def return_snafu(inp: int) -> int:
    outstring = ""
    n = 0
    while inp >= 5**n and inp >= 5**(n+1):
        n += 1
    if inp > power_sum(n):
        outstring += "1"
        outstring += inverter(5**(n+1)-inp, n+1)
    else:
        outstring += inverter(inp, n)
    return outstring

"""
5^n, 5^n-1, ... 5^2, 5^1, 5^0
num = len(str(inp))
def inverter(inp, num):
    
if inp > 
-2 -> =
-1 -> -
0 -> 0
1 -> 1
2 -> 2
3 -> 1=
4 -> 1-
5 -> 10
6 -> 11
7 -> 12
8 -> 2=
9 -> 2-
10 -> 20
11 -> 21
12 -> 22
13 -> 1==

17 + 2 == 19 -> 1--
if inp < 3:
    if inp == 2:
        return "2"
    elif inp == 1:
        return "1"
    elif inp == 0:
        return 0
    elif inp == -1:
        return "-"
    elif inp == -2:
        return "="
    else: 
        return "garbage"
elif inp < 5**n - 2*5**(n-1):
    run_function(inp, n-1)

if inp < 5**(num+1) and inp > 5**(2*num):
    outstring += "2"
    inverter(inp - 2*5**2, num-1)
elif inp == 5**(2*num):
    return "2"
elif inp > 5**num and inp < 5**(2*num):
    outstring += "1"
    inverter(inp - 5**2, num-1)
elif inp == 5**(num):
    return 1
elif inp < 5**num and inp < 5**(2*num):
    outstring += "1"
    inverter(inp - 5**2, num-1)
elif 

elif inp > 5**num and inp < 5**(2*num):
    outstring += "1"
    inverter(inp - 5**2, num-1)
elif
elif inp > 5**num and inp < 5**(2*num):
    outstring += "1"
    inverter(inp - 5**2, num-1)

33 >25 < 50 -> "1" 
"""


def inverter(inp: int, num) -> str:
    outString = ""
    if inp < 3:
        if inp not in int_map:
            return "garbage"
        return int_map[int]
    elif inp < power_sum(num-1):
        subt = 0
    elif inp >= 2*5**num and inp <= power_sum(num):
        outString += "2"
        subt = 2*5**num
    elif inp >= 5**num and inp < 2*5**num:
        outString += "1"
        subt = 5**num
    elif inp > 1:
        return 'none'

    outString += inverter(inp-subt, num-1)


def readInfile(inFile):
    outSum = 0
    with open(inFile) as f:
        for line in f.readlines():
            outSum += converter(line.rstrip())
    print(outSum)
    return outSum

def main():
    readInfile("input.txt")

if __name__ == "__main__":
    main()