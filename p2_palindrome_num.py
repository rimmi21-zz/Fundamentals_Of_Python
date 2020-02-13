#Check if num is plaindrome

num=int(input("Enter the number: "))
num_str=str(num) #Type-casting the number to String
flag=0
#No need to iterate throught the whole of string
#Just iterate till the half of the string
#If the last two match it is automatically a reverse

for i in range(len(num_str)//2): #halfing the list
    if num_str[i]!=num_str[len(num_str)-i-1]:
        flag=1 #Check till that point till it is not equal
        break #As soon as u reach that point break & get out
if flag==1:
    print("Not a Plaindrome")
else:
    print("Palindrome") #It could be a plaindrome because the above iteration could occur successfully
