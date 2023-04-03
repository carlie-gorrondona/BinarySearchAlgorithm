#---------------------- FUNCTIONS ----------------------#
# This function generates the number list array that stores values from 0 to 100 as long as they are mulitples of 2. Once the array has all values stored, it returns the array
# so it can be passed to the binarySearch() function. 
def createNumberList():
    numberList = []
    newNumber = 0

    while newNumber < 101:
        numberList.append(newNumber)
        newNumber += 2

    print(numberList)
    return numberList
    
    
# This function takes the numberList array and userInput to locate the number the user wants to find in the array. A lowPoint variable is set to zero and a highPoint variable
# is set to the length of the numberList array minus one. The while loop runs as long as lowPoint is less than or equal to highPoint. Inside the loop, a midPoint variable is 
# set to the sum of the lowPoint and highPoint divided by two which represents the middle index of the numberList array. If the number at index midPoint equals userInput, 
# then the number has been located and a message stating the number has been found prints to the terminal. If the number at index midPoint is less than userInput, then lowPoint
# is set to the midPoint plus 1. If the number at index midPoint is greater than userInput, then highPoint is set to the midPoint minus one. If the number is not located, then
# negative one prints to the terminal.
def binarySearch(numberList, userInput):
    userInput = int(userInput)
    lowPoint = 0
    highPoint = len(numberList) - 1

    while lowPoint <= highPoint:
        midPoint = (lowPoint + highPoint) // 2

        if numberList[midPoint] == userInput:
            print("Your number (" + str(userInput) + ") was located at index " + str(midPoint))
            return midPoint
        elif numberList[midPoint] < userInput:
            lowPoint = midPoint + 1
        else:
            highPoint = midPoint - 1

    return -1
    

#---------------------- MAIN ----------------------#
print("Enter a number between 0 and 100 you would like to search for.")
userInput = input("Your number: ")

numberList = createNumberList()
binarySearch(numberList, userInput)
