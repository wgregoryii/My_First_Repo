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
intToroman = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
              50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
userNumber = int(input("Enter a number: "))

#Descending intger equivalent of seven roman numerals 
print_order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

for userProvidednumber in print_order:
    if userNumber != 0:
        leftOver= userNumber//userProvidednumber

        #If quotient is not zero output the roman equivalent
        if leftOver != 0:
            for y in range(leftOver):
                print(intToroman[userProvidednumber], end="")

        #update integer with remainder
        userNumber = userNumber%userProvidednumber