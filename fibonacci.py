n = int(input("Enter the no. of terms you want to be displayed:"))
num1=0
num2=1
count =0
if n<=0:
    print("Enter positive no.s only!")
elif n==1:
    print(num1)
else:
    while count< n:
        print(num1)
        temp = num1+num2
        num1=num2
        num2=temp
        count+=1
 
