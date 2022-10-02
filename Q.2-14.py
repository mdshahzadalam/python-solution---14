#2. Write a Python script to create a list of first N odd natural numbers.
n=int(input("enter the numbers"))
l1=[]
#i=0
for i in range(1,2*n,2):
    l1.append(i)
print(l1)