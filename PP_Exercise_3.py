# Take a list, say for example this one:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(i for i in a if i < 5)

a_sort = sorted(a)
print(a_sort)

a_sort_five = sorted(i for i in a_sort if i < 5)

print(a_sort_five)

#Extras:

#--> Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#+ Write this in one line of Python.
#--> Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

provided_num = float(input("Please enter a number: "))

# [output] for [item] in [list] if [filter]

print(i for i in a if i < provided_num)