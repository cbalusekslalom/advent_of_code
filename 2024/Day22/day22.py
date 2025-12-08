import numpy as np
# multiply by 64, then mix into secret (XOR bitmap), then prune (mod 16777216)
# int(/32) then mix then prune
# multiply by 2048 then mix then prun
# new secret

def mix(secret, inVal):
    return secret ^ inVal

def mod(secret):
    return secret%16777216

def iterate(secret):
    s = secret
    v = s*64
    s = mix(s,v)
    s = mod(s)
    v = int(np.floor(s/32))
    s = mix(s,v)
    s = mod(s)
    v = s*2048
    s = mix(s,v)
    s = mod(s)
    print(s%10)
    return s

def main(inFile):
    inList = []
    with open(inFile) as f:
        for line in f.readlines():
            inList.append(int(line.strip()))
    result = map(iterate, inList)
    for i in range(1,2000):
        result = map(iterate, result)
    print(sum(result))

if __name__ =="__main__":
    main('input_files/day22_input.txt')