def safeOrUnSafe(input):
    countDCounter = 0
    countACounter = 0
    for xid,x in enumerate(input[1:len(input)]):
        diff = abs(int(input[xid]) - int(input[xid+1]))
        if((int(input[xid]) < int(input[xid+1])) and diff >= 1 and diff <=3):
            countDCounter = countDCounter + 1
        elif((int(input[xid]) > int(input[xid+1])) and diff >= 1 and diff <=3):
            countACounter = countACounter + 1
    return countDCounter, countACounter

def main():
    with open("input.txt", "r") as file:
        arr = []
        dcounter = False
        acounter = False
        diff = 0
        prevDirection = 0
        countDCounter = 0
        countACounter = 0
        for y in file:
            input = y.split()
            countDCounter, countACounter = safeOrUnSafe(input)
            if(countACounter == (len(input) - 1)):
                acounter = True
            elif(countDCounter == (len(input) - 1)):
                dcounter = True
            if(acounter == True or dcounter == True):
                arr.append("1")
            else:
                arr.append("0")
            countACounter = 0
            countDCounter = 0
            dcounter = False
            acounter = False
        summation = 0
        for num in arr:
            numFromArray = int(num)
            summation = summation + numFromArray
        print(summation)
if __name__ == "__main__":
    main()