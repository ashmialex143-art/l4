a=int(input("enter your amount:"))
n1=a//500
n2=((a%500)//100)
n3=(((a%500)%100)//50)

print("500 rupees note:",n1)
print("100 rupees note:",n2)
print("50 rupees note:",n3)