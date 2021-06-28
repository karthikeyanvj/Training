#Integer method

s=input("Enter a number: ")
p=(s[::-1])
if p==s:    
    print("The number is a palindrome")
else:
    print("Not a palnidrome")"""
--------------------------------------------------------    
#string method

a=input("Enter a name: ")
b=a
c=(b[::-1])
if b==c:
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")
    
# using for loop

number=input("Enter any number :")
i=0
for i in range(len(number)):
    if number[i]!=number[-1-i]:
        print('It is not a palindrome')
        break
    else:
        print('It is a palindrome')
        break
