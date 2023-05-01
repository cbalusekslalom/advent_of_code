
def check_dups(inList):
    if len(set(inList)) != len(inList):
        return False
    return True


def packet_scanner(inList: list):
    for i in range(14, len(inList)-1):
        check_list = inList[i-14:i]
        print(f"now running {i}. elements are {check_list}")
        print(f"Len of set is {len(set(check_list))}. Len of list is {len(check_list)}")
        if check_dups(check_list):
            print(i)
            break

def main():
    with open('input.txt', 'r') as f:
        inputList = [i for i in f.readline()]
    print(inputList)
    packet_scanner(inputList)

if __name__ == '__main__':
    main()
