"""simple calculator and no details"""
ask=int(input("enter a no:"))


print(len(str(ask)),"long no")


yo=(
if ask > 0:
    print(ask,"postive no")
elif ask < 0:
    print(ask,"negative no")
else:
    print("zero")
)

    
if ask%2==0:
    print(ask,"even no")
else:
    print(ask,"odd no")



s=str(ask)
for i in range(len(s)-1,-1,-1):
    print(s[i])



if ask<=1:
    print("not prime")
else:
    prime=True

    for i in range(2,ask):
        if ask%i==0:
            prime=False
            break
    if prime:
        print("prime no")
    else:
        print("not prime")
          
total=0
for prime in str(ask):
    total+=int(prime)
print(prime,"=digit" ,total,":total")


largest=0
for ldigit in str(ask):
    lm=int(ldigit)
    if lm>largest:
        largest=lm

print(lm,"largest digit")





smallest = int(str(ask)[0])

for sdigit in str(ask):
    it = int(sdigit)

    if it < smallest:
        smallest = it

print(smallest, "smallest digit")
    
            
