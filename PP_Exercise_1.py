# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# -->   Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# -->   Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = str(input("What is your name: "))
age  = int(input("What is your age: "))
year = (2019 - age) + 100

answer = name + " will turn 100 in the year " + str(year) 

print(answer)

# Add on I

runningtimes = int(input("How many times do you want to see this message: "))

print(runningtimes)

print((answer + ' ' )* runningtimes)