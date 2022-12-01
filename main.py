
'''
Functions:
Mean
Median
Mode 
Range
Medan Deviation
Stdandard Deviation
'''


def getMean(lst):
    return sum(lst) / len(lst)

def getMedian(lst):   
    midPoint = len(lst) // 2
    med = ((lst[midPoint]) + (lst[-midPoint-1])) / 2
    return med

def getMode(lst):
    unique = list(set(lst))
    mode_count = 0 
    max_count = 0 
    current_mode = lst[0]

    for i in unique:
        for j in lst :
            if i == j :
                mode_count += 1
        if mode_count > max_count :
            max_count = mode_count 
            current_mode = i

        mode_count = 0 

    return current_mode
        
def getRange(lst):
    lst.sort()
    range = lst[-1] - lst[0]
    return range

def getStDev(lst):
    dev = []
    mean = getMean(lst)
    for i in lst:
        dev.append((mean - i)**2)

    totalDev = sum(dev)
    stdDev = (totalDev / mean)**0.5

    return stdDev

def getMeanDeviation(lst):
    mean = getMean(lst)
    deviations = []
    for i in lst:
        deviations.append(abs(mean-i))
    meanDeviation = getMean(deviations)
    return meanDeviation
    


    
while True:
    print()
    print("Operations available : ")
    print("-------------------------------")
    print("1 -> mean")
    print()
    print("2 -> range")
    print()
    print("3 -> standard deviation")
    print()
    print("4 -> mode")
    print()
    print("5 -> median")
    print()
    print("6 -> mean deviation")
    print()
    print("7 -> Exit program")
    print("-------------------------------")

    mainMenuChoice = input("Enter your choice : ")

    if mainMenuChoice == "7":
        print("Thank you")
        break

    values = list(
        map(float,
            input("Enter values seperated with spaces :").split()))

    if mainMenuChoice == '1':
        answer = getMean(values)
        print("Mean of given values is :", answer)

    elif mainMenuChoice == '2':
        range = getRange(values)
        print("Range of the given dataset is: ", range)

    elif mainMenuChoice == "3":
        stdDev = getStDev(values)
        print("Standard deviation of given values is: ", stdDev)
        
    elif mainMenuChoice =='4':
        mode = getMode(values)
        if mode == 1:
            print(' No determined mode')
        else:
            print('Mode is ', mode)
        
    elif mainMenuChoice == '5':
        median = getMedian(values)
        print('Median of given values is ', median)

    elif mainMenuChoice =='6':
        meanDeviation = getMeanDeviation(values)
        print('mean deviation of given values is ', meanDeviation)