#9. Write a Python script to print indices of all occurrences of a given element in a given
#   list.
#   occurrence in the list.
l1=[eval(x) for x in input("enter list elements:-").split(',')]
element =eval(input('enter element value:-'))
index=0
while index<len(l1):
  if l1[index]==element:
     print(index,end=' ')
  index+=1
