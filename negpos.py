number_list = []
n = int(input("Enter the list size "))
print("-----------------\n")
for i in range(0, n):
    print("Enter number at index", i)
    item = int(input("Enter:"))
    number_list.append(item)
print("User list is ", number_list)
print('-------------')
neglist=[]
poslist=[]
for i in number_list:
    if i<0:
        b=i
        neglist.append(b)
    elif i>0:
        c=i
        poslist.append(c)    
print("Negative numbers are in the given list",neglist)
print()
print("Positive numbers are in the given list",poslist)
