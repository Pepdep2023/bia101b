# a calculator application made using terminal
# variables and if statements

# 1. get-input from user
# 2. do calculation based on user-input
# 3. give output to the user


print('* multiplication')
print('+ addition')
print('- subtraction')
print('/ division')

whatUsertyped = input()
 
print('User typed',whatUsertyped)
print('user input type',type (whatUsertyped))

if whatUsertyped == "+":
    print('Doing addition')
    print('doing more addition')


if whatUsertyped == "-":
    print('doing subtraction')
    print('doing more substraction')



print('-------------------')
if whatUsertyped == "+":
    print('Doing Addition')
    if 'a' == 'b':
        print('a is not b')
    if 'b' == 'b':
        print('b is b')

# Objective: a calculator application made using 
# variables and if statements

# STEPS
# 1. get input from user --> DONE

# 2. do calculation based on user input
# 2.1 check what string did user typed
# 2.2 if usser string == * then do multiplicatio and so on

# 3. give output to the user

print('* for multipliocation')
print('+ for addition')
print('- for subtraction')
print('/ for division')

whatUserTyped = input()

print('User typed:', whatUserTyped)
print('user input-type', type(whatUserTyped))

print('-------------------')
if whatUserTyped == "+":
    print('Doing Addition')
    if 'a' == 'b':
        print('a is not b')
    if 'b' == 'b':
        print('b is b')

print('doing more addition')

if whatUserTyped == "-":
    print('Doing Subtraction')
    print('doing more subtraction')