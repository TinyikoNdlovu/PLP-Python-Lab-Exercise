# Write a program that asks the user for their 
# name, age, and location and then prints out a 
# personalized message.

name = input("Please enter your name: ")
age = int(input("Enter your age: "))
location = input("Please enter your location: ")

print('Hello {}, you are {} years old and live in {}.'.format(name, age, location))

