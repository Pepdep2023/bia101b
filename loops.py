# loop over an array
fruits = ['a', 'b', 'c']

# loop through each evelement
# at each stage, if the element is 'a'
# print true
for e in fruits:
    if e == 'a':
        print('True')

# loop through each evelement
# at each stage, if the element is 'c'
# print true
for e in fruits: # 1.e = 'a', 2.e = 'b 3. e = 'c'
    if e == 'c':
        print('True')
    if e == 'b':
        print('True') 

# # Iterate over a string -for loop
greeting = "Hello"
for char in greeting:
    print(char)
    # Exercise: check if the string contains vowel

#Iterate over a range(20times)
for i in range(9,14): #5 -13
    print(i)


# # # Iterate over a string
# greeting = "Hello"
# for char in greeting:
#     print(char)
#     # Exercise: check if the string contains vowel




# Iterate over a range
# for i in range(5,14,2): #  5 - 13
#     print(i)






# Iterate over a range with step
# for i in range(0, 10, 2):
#     print(i)  # Output: 0 2 4 6 8


#! While Loops
# Basic while loop

count = 0
while count < 5:
    # print(count)
    count = count + 1  # Output: 0 1 2 3 4

# user input string is unknown
# print every char of the string
s = 'helloabc'
counter = 0
lenth_s = len(s)
print('coutner:', counter)
print('len s:', lenth_s)
# 0 , 1 , 2, 3, 
print('going in loop')
while counter < lenth_s:
    print('counter:', counter)
    char = s[counter]
    print(char)
    counter = counter + 1
    print('-----')
#! 30 MINS
#! For Loops
# Iterate over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Iterate over a string
greeting = "Hello"
for char in greeting:
    print(char)

# Iterate over a range
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# Iterate over a range with step
for i in range(0, 10, 2):
    print(i)  # Output: 0 2 4 6 8

#! While Loops
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1  # Output: 0 1 2 3 4

# Break statement
number = 0
while True:
    if number == 5:
        break
    print(number)
    number += 1  # Output: 0 1 2 3 4

# Continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Output: 1 3 5 7 9

#! Nested Loops
# Nested for loop
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# Output:
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)

# Nested while loop
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(f"({i}, {j})")
        j += 1
    i += 1


    
