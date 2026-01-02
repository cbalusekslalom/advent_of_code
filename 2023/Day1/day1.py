import os, sys

##pt2
def ConvertString(inLine:str) -> str:
    convert_dict = {"o":{"one":"1"},
                    "t":{"two":"2","three":"3"},
                    "f":{"four":"4","five":"5"},
                    "s":{"six":"6","seven":"7"},
                    "e":{"eight":"8"},
                    "n":{"nine":"9"}
                    ,"z": {"zero":"0"}
    }
    i = 0
    while i < len(inLine)-2:
        if inLine[i] not in convert_dict.keys():
            i += 1
            continue
        for subkey in convert_dict[inLine[i]].keys():
            if len(inLine[i:-1])+1 < len(subkey):
                i+=1
                continue
            if inLine[i:i+len(subkey)] == subkey:
                inLine = inLine[:i] + convert_dict[inLine[i]][subkey] + inLine [i+1:]
                i+=1
                continue
        i+=1
                
    return inLine
    

## pt1
def convertChars(inLine: str) -> int:
    ## o:1, t:2, f:2, s:2, e: 1, n: 1, z:1
    convert_dict = {
                    "one":"1","two":"2","three":"3","four":"4","five":"5",
                    "six":"6","seven":"7","eight":"8","nine":"9","zero":"0"
                    }
    outList = []
    for x in convert_dict.keys():
        if x in inLine:
            outList.append(inLine.replace(x, convert_dict[x]))
    # print(outList)
    return inLine

## [int(j) for j in [i for i in inLine] if j.isdigit()]

def procLine(inLine: str, pt2 = False) -> int:
    if pt2:
        res2 = [int(j) for j in [i for i in ConvertString(inLine)] if j.isdigit()]
        #print(f"{inLine} maps to: {res2} and a total of {res2[0]*10 + res2[-1]}")
    else:
        res2 = [int(j) for j in [i for i in convertChars(inLine)] if j.isdigit()]
    # print(f"{res2} maps to: {res2[0]*10 + res2[-1]}")
    return [res2[0]*10 + res2[-1], res2]

def main(input_filepath: str, output: str, pt2 = False) -> int :
    totalSum = 0
    #outList = []
    outfile = open(output, 'a')
    with open(input_filepath, 'r') as inFile:
        for line in inFile.readlines():
            proc_out = procLine(line,pt2=pt2)
            #outList.append(procLine(line,pt2=pt2))
            totalSum += proc_out[0]
            outfile.write(f"{line.strip()} \t\t {proc_out[1]} \t\t {proc_out[1][0]}{proc_out[1][-1]}\t {totalSum} \n")
    print(f"The total of all lines is: {totalSum}")
    #return outList
    outfile.close()


if __name__ == "main":
    main()
