'''
#TASKFirst: 10.1
Second: 20
Sum: 30.1
'''
'''first = input("First: ")
second = input("Seconds: ")
sum = float(first) + float(second)
print("Sum: " + str(sum))
'''
'''
course = 'Python for Beginners'
print(course.upper())
print(course)
'''

'''
course = 'Python for Beginners'
print(course.lower())
print(course)
'''

'''
course = 'Python for Beginners'
print(course.find('y'))
print(course)
'''

'''
course = 'Python for Beginners'
print(course.find('Y'))
'''

'''
course = 'Python for Beginners'
print(course.find('for'))
'''

'''
course = 'Python for Beginners'
print(course.replace('for', '4'))
print(course)
'''

'''
course = 'Python for Beginners'
print('Python' in course)
'''

'''
print(10 + 3)
'''

'''Option are '+' '-' '*' '/'(decimal #) '//'(integer #) '%'("Modulus Pperator" remainder of division) and '**' (to the power of) '''

'''Solving for variables
x = 10
y = x + 3
SAME AS BELOW
x += 3 
The 3 is first added, then it is totaled'''

'''
x = 10 + 3 * 2
print(x)

x = (10 + 3) * 2
print(x)
'''

'''
These are the operators. 
>
>+
<
<=
==
!+

x = 3 != 2
print(x)
'''
"""
price = 5
print(not price > 10)
"""

"""temporature = 66

if temporature > 75:
    print("It's a hot day")
    print("Drink plenty of water")
elif temporature > 65: # (20,3]
    print("It's a nice day")
elif temporature > 55: # (10, 20])
    print("It's a bit cold")
else:
    print("It's cold")
print("Done")
"""

'''
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))
    '''

#Print numbers
'''i = 1
while i <= 100:
    print(i * '*')
    i = i +1
'''

#Types of data
'''
Numers = whole numbers
Floats = decimal numbers
Boolean = True, Flase
Strings = Text DeprecationWarning
'''

# Complex types of data - LISTS
'''
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0] = "Jon"
print(names[0:3])
print(names)
'''
numbers = [1, 2, 3, 4, 5, 6]
numbers.insert (0, -1)
print(numbers)
