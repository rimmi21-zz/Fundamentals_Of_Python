#code to find the sum of numbers divisible by 4
sum=0
while True: #Taking while as true so that sum can iterate infinitely
    num=int(input("Enter your number: "))
    if num%4==0:
        sum+=num
    ch=input("Wanna continue? (Y/N) ")
    if ch.upper()=='N':
        break
print(sum)
