#2. 3. Write a Python script to create a list of first N even natural numbers.
n=int(input("enter the numbers"))
l1=[]
#i=0
for i in range(2,2*n+1,2):
    l1.append(i)
print(l1)