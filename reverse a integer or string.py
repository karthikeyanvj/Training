#reverse a string

def reverse():
    s=input("Enter a string: ")
    r=(s[::-1])
    if s==r:
        print(s,"is a Palindrome")
    else:
        print(s,"not a palindrome")
    print(s,"This is the original string")
    print(r,"this is the reverse of a string")
reverse()

# using recursive method
"""def reverse(s):
    if len(s)== 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
s=input("enter")
print("the original:",end="")
print(s)
print("the original:",end="")
print(reverse(s))"""



