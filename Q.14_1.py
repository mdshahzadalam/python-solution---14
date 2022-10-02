#1. Write a Python script to create a list of first N natural numbers.
print("how many numbers do you want to enter ")
n=int(input())
print("enter some numbers:-")
l1=[]
i=0
while i<n:
    l1.append(int(input()))
    i+=1
print(l1)