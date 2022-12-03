# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument
num1=int(input("Enter the number:"))
result=lambda num1:num1+25
print(int(result(num1)))