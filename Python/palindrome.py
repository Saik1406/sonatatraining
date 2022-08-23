'''n=int(input("enter a number:"))
reverse_number=n
r=0
while n!=0:
    temp=n%10
    r=r*10+temp
    n=n//10
if(reverse_number==r):
    print("palindrome",r)
else:
    print("not palindrome",r)'''

n=input("enter a number:") #THis is another method
reversed_number=n[::-1]
if(reversed_number==n):
    print("the given number",reversed_number,"is palindrome")
else:
    print("the given number is",reversed_number,"not palindrome")



