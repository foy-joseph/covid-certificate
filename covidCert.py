import random

# generate and return a string of 6 random digits (0 to 9).
def getRandomStr():
    strOut = int(0)
    tens=1 #set a control for the digit placing
    for d in range(0, 6):
        strOut += tens*random.randint(0, 9)
        tens*=10 # multiply the next digit by 10 so it will add to the 
    strOut=str(strOut)
    if len(strOut) == 5:
        strOut = "0",strOut
    return str(strOut)

# compute and return the check digit for a random sequence passed as an argument
# sequence of 6 digits in a string passed in as an argument
def calcCheckDigit(strIn):
    d7 = 0
    num = len(strIn)
    num2 = len(strIn)
    for v in range(0, num2):    
        d7+=(int(strIn[v])*num)
        num-=1
    d7=d7%10 # find the last digit in the integer
    return d7
#generate a full covid ID
def generateCovidId(vacType):
    vacType = vacType.upper()
    strOut = str('')
    if vacType == "AZ":
        strOut+=("AZ")
    elif vacType == "MO":
        strOut+=("MO")
    elif vacType == "JA":
        strOut+=("JA")
    elif vacType == "PF":
        strOut+=("PF")
    sixDigits = getRandomStr()
    strOut = str(strOut) + str(sixDigits) + str(calcCheckDigit(str(sixDigits)))
    return strOut

#validate covid certificate using 'if' statements and the other predefined methods.
def validateCovidId(strIn):
    isItValid = False
    # first check if the length of the id has 9 characters
    if len(strIn) == 9:
        # validate first two letters of the ID
        validateTwoLetters = False
        validExistingIds = ["AZ", "MO", "JA", "PF"]
        while not validateTwoLetters : # loop until user enters valid two digits.
            for twoDigitType in validExistingIds: # loop through the valid types and check if input matches
                if twoDigitType == strIn[0:2].upper():
                    validateTwoLetters = True
        # validate the next 6 digits of the ID
        sixDigitsCheck = False
        if strIn[2:9].isnumeric():
            sixDigitsCheck = True
        # validate the last digit (security digit)
        lastDigitCheck = False
        if strIn[9] == calcCheckDigit(strIn[2:9]):
            lastDigitCheck = True
        # check if all three checks returned true
        if validateTwoLetters and sixDigitsCheck and lastDigitCheck:
            isItValid = True
    return isItValid


existingIds = [] # create a list of all CovidCert IDs given to patients.

def getPplWithVacType(checkTypeIn):
    listOfSimilarIds = []
    for twoDigitType in existingIds:
        if twoDigitType[0:2] == checkTypeIn.upper():
            listOfSimilarIds.append(twoDigitType)
    return listOfSimilarIds

# The program must first validate the entry made by the user
def collectAndValidateUserInput():
    vacTypeList = ["AZ", "MO", "JA", "PF"]
    vacTypeIn = input("Enter vaccine type: \n[AZ]-AstraZenica\n[MO]-Moderna\n[JA]-Janssen\n[PF]-Pfizer/BioNTech\n")
    inputValidCheck=False
    while not inputValidCheck : # loop until user enters valid two digits.
        for twoDigitType in vacTypeList: # loop through the valid types and check if input matches
            if twoDigitType == vacTypeIn.upper():
                inputValidCheck = True # break out of the loop when id is generated
    return vacTypeIn # when the loop breaks, the user-entered string is valid and will be returned

def doesItExistFunc(tempId):
    doesItExistCheck = True
    for existingIdStrings in existingIds:# iterate through existing Ids
        if existingIdStrings == tempId:
            doesItExistCheck = False
    return doesItExistCheck

isTheVaccinatorFinished = False
while not isTheVaccinatorFinished:
    enteredId = generateCovidId(collectAndValidateUserInput())# An id is generated along with the function above - collectAndValidateUserInput().
    print("Your unique CovidCert ID: " + enteredId)
    if not doesItExistFunc(enteredId):
        existingIds.append(enteredId) # store the generated Id into the existing list of Ids
    if input("Stop Vaccinating?\n[Y/N] ").lower() == "y":
        isTheVaccinatorFinished = True



idsAtTheBall = [] # create a list to store existing student at the ball

def getIndexOfExistingId(existingIdIn): # create function to return the index of identical covid cert ids
    for i in idsAtTheBall: # iterate through the ids at the ball. if the id inside the ball is the same as the argument, find the index of the Id by re-iterating through the Ids inside.
        if i == existingIdIn:
            for j in range(0, idsAtTheBall):
                if i == idsAtTheBall[j]:
                    return j

loopContinues = True
while loopContinues: # initiate a loop
    print("Welcome to the LYIT Christmas Ball")
    studentIdIn = input("Please enter your CovidCertID: (Enter [exit] to exit) ") # a. Prompt the user to enter a CovidCert ID. 
    if studentIdIn.lower() == "exit":
        break # the loop only breaks if the user enters "exit"
    if validateCovidId(studentIdIn): # b. Validate it
        if doesItExistFunc(studentIdIn): # c. If it is valid check if it is already in the list. 
            for i in idsAtTheBall: # d. If it is in the list give the index or position in list.
                print("The ID entered exists at index " + getIndexOfExistingId(studentIdIn) + "\nRe-enter a valid, unused ID")
        else: 
            idsAtTheBall.append(studentIdIn) # e. If it is not in the list, add it to the list.
            print("Enjoy your night")
    else:
        print("Invalid ID - Please try again")