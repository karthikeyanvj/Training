esum=0
osum=0
a=int(input("Enter the number: "))
for i in range(0,a+1):
    if i%2==0:
        esum=esum+i
    else:
        osum=osum+i
print("Sum of even number from 0 to " + str(a),':',esum)
print("Sum of odd number from 0 to " + str(a),':',osum)
    
    
        
    
