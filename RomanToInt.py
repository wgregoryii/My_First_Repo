#optional solution: 
#class Solution:
#    def intToRoman(self, num: int) -> str:
#        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D",500], ["CM", 900], ["M", 1000]]
#
#        res = ""
#        for sym, val in reversed(symList):
#            if num // val:
#                count = num // val 
#                (sym * count)
#                num = num % val

#Integer to Roman Number Converter
#integerToromantable = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
#              50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
#userInputnumber = int(input("Enter a number: "))

#Descending intger equivalent of seven roman numerals 
#loop_read_order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

#Define "userProvidednumber" for loop
#for userProvidednumber in loop_read_order:
#    if userInputnumber != 0: #If the users number does NOT equal zero define "leftOver"
#        leftOver= userInputnumber//userProvidednumber #Divide the "userInputnumber" by the "userProvidednumber" to get the "leftOver"
#
#        #If the "leftOver" is not zero output the roman equivalent
#        if leftOver != 0:
#            for number in range(leftOver):
#                print(integerToromantable[userProvidednumber], end="")
#
#        #update integer with "leftOver""
#        userInputnumber = userInputnumber%userProvidednumber #leftOver returns to loop until it equals zerto

"""
https://pencilprogrammer.com/python-programs/convert-integer-to-roman-numerals/
https://stackoverflow.com/questions/28777219/basic-program-to-convert-integer-to-roman-numerals
https://leetcode.com/problems/integer-to-roman/discuss/6304/Python-simple-solution.
"""
def convertIntRomanNumeral(num):
    romanNumbers = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 
            50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
    num_to_roman = ""
    for i in romanNumbers.keys():
        num_to_roman += romanNumbers[i] * (num // i)
        num %= i
    return num_to_roman
message = """
Enter a number between 1 and 3999 to be converted to Roman numerals.
To exit, please type "exit."\n
"""
errMessage = "Not Valid Input!!!"
while True:
    numToConvert = input(message)
    if numToConvert.lower() == 'exit':
        print("exit was entered - exiting the program")
        break
    
    if numToConvert.isdecimal() == False:
        print(f"{numToConvert}  {errMessage}")
    else:    
        if int(numToConvert) <= 0 or int(numToConvert) > 3499:
            print(errMessage)
            continue
        else:
            #numToConvert = int(numToConvert)
            print(f"Roman Numeral for {numToConvert} is {convertIntRomanNumeral(int(numToConvert))}")