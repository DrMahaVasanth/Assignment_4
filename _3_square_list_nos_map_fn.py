# Write a Python program to square the elements of a list using map() function.
size=int(input("Enter the size of the list:"))
lst=[]

for i in range(size):
    num=int(input("Enter the number:"))
    lst.append(num)
print("original list:",lst)

# without using lambda function:
def square(data):
    return data**2
sq_lst=list(map(square,lst))
print("Squared list using map function:",sq_lst)

# with using lambda
sq_lst=list(map(lambda data:data**2,lst))
print("Squared list using map and lambda functions:",sq_lst)