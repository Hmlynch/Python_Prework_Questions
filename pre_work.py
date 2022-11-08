#Question 1:
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
#def hello_name(user_name):

hello_name = input('Username:')
print("Hello " + hello_name)

#Question 2:
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
#def first_odds():

odd_num = range(1,100)
for i in odd_num:
    if i % 2 != 0:  # "!=" means not equal # "%" means remainder of x / y
        print(i, end=" ")

#Question 3:
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
# def max_num_in_list(a_list):

a_list = [2, 8, 19, 22, 31, 45, 63, 99]
max_num_in_list = max(a_list)
print(max_num_in_list)

#Question 4:
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
#def is_leap_year(a_year):

a_year = input('year: ')
is_leap_year = int(a_year)
if (is_leap_year % 4 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

#Question 5:
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
#def is_consecutive(a_list):

a_list = [2,3,4,5,6,7,9]
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))
print(is_consecutive(a_list))

