# Check if user can vote

#1. get user input
userInput =input("Please enter your age: ")

#2. convert user input to number
userage = int (userInput)

#3.check if user can vote
if userage >= 18:
    print("You can vote")
else:
    print("You cannot vote")
    
#3. check if user can vote
if userage >= 18:
    print("You can vote")
elif userage < 18:
    print("You cannot vote")
