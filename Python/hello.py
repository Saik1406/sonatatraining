n=int(input("enter a numebr:"))
r=0
temp=n
while temp>0:

    r=r+(temp%10)*(temp%10)*(temp%10)
    temp=temp//10

if(n==r):
    print("armstrong",r)
else:
    print("not armstrong")