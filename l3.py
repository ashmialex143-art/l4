print("enter your marks:")
eng=int(input("eng:"))
math=int(input("math:"))
sci=int(input("sci:"))

sum=eng+math+sci
print("sum:",sum)

per=int((sum/300)*100)
print("percentage:", per , end="%")
