print("Enter Your Marks")
Maths=int(input("enter your marks in math: "))
science=int(input("enter your marks in science: "))
english=int(input("enter your english marks: "))
arabic=int(input("enter your arabic marks: "))
MSC=int(input("enter your MSC marks: "))
sum=Maths+science+arabic+MSC+english
print(sum)
percentage=(sum/500)*100
print("your total percentage is",percentage,"%")