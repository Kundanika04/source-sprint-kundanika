a,b = map(int, input("Enter the two space separated integers:\n").split())
s=input("Enter the operator:\n")
if(s=='+'):
    print(a+b)
elif(s=='-'):
    print(a-b)
elif(s=='/'):
    print(a/b)
elif(s=='*'):
    print(a*b)
else:
    print("Enter the correct operator.\n")
print("Thank you.\n")
print("Final statement")
