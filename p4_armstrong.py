#Armstrong number is a number that is equal to the sum of cubes of its digits.
n=int(input("Enter your number: "))
temp=n
count=0
while temp!=0:
    temp=temp//10
    count+=1

temp=n
sum=0
while temp !=0:
    digit=temp%10
    temp=temp//10
    sum=sum+digit**count

if sum==n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
