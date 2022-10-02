#8. Write a Python script to print distinct elements along with their frequencies of
#   occurrence in the list.

l1=[10,"shahzad",24,"alam",10,10,"kako",5,"patna",4,3,"raju"]

frequency={}
for item in l1:
    if item in frequency:
      frequency[item]+=1
    else:
        frequency[item]=1
print(frequency)



