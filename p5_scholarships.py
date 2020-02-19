#code to calculate and display the final fees to be paid by each student wrt score and fees with scholarship
while True:
    branch=input("A or B?")
    score=int(input("Enter the student's score: "))
    fees=int(input("Enter the fees for the course: "))
    scholarships=[0,0]
    if branch.upper()=='A':
        if score>=90:
            scholarships[0]=0.5
        if score%2!=0:
            scholarships[1]=0.05
    elif branch.upper()=='0':
        if score>85:
            scholarships[0]=0.5
        if score%7==0:
            scholarships[1]=0.05
    max_scholarship=max(scholarships)
    final_fee=fees-fees*max_scholarship
    print(final_fee)
    ch=input("Do you want to continue? [Y/N]")
    if ch.lower()=='n':
        break
        
