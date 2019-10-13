#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
#Extras:
#
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


#Asking for input

provided_number = int(input("What is the number in your mind: "))
divided_number = provided_number % 2

print("You have chosen " + str(provided_number) + " as your number")

#Providing answer
# FIXME
#try: 
 #  answer = int(divided_number)
 #  print("You have chosen an even number!")
 #  print("You had chosen: ", provided_number)
#except ValueError:
 #  print("That's an odd number!") # Not working for now 
 #  print("You had chosen: ", provided_number)


#Providing answer V.2

if divided_number == 0:
    print("You picked an even number.")
else:
    print("You picked an odd number.")

#If the number is a multiple of 4, print out a different message.

multiple_4 = provided_number % 4

if multiple_4 == 0:
      print("You chose a multiple of 4, how exciting!")

#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

print("Now let's try something else")

sum = int(input("Pick another number!: "))
check = int(input("Now pick another one: "))

sum_div = sum / check

if sum_div % 1 ==0 :
      print("Your first number devided by the second number is an integer, namely " +str(sum_div))

else:
         print("Your first number divided by the second number is not an integer, namely " +str(sum_div))
