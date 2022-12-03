# Write a Python program to triple all numbers of a given list of integers. Use Python map
size=int(input("Enter the size of the list:"))
lst=[]

for i in range(size):
    num=int(input("Enter the number:"))
    lst.append(num)
print("original list:",lst)

# without using lambda:
def triple(data):
    return data*3
tri_lst=list(map(triple,lst))
print("Tripled list using map function:",tri_lst)

# with lambda function
tri_lst=list(map(lambda data:data*3,lst))
print("Tripled list using map and lambda functions:",tri_lst)