#Code to find the minimum among 3 numbers

num1=int(input("Enter the first number: ")) #Input Number1
num2=int(input("Enter the second number: ")) #Input Number2
num3=int(input("Enter the third number: ")) #Input Number3

if num1<num2:
    if num1<num3:
        print(num1)
    else:
        print(num3)
elif num2<num3:
    print(num2)
else:
    print(num3)
