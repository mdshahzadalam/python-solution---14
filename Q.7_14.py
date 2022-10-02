#7. Write a Python script to remove all non int values from a list.

l1=[10,"shahzad",24,"alam",6,8,"kako",5,"patna",4,3,"raju"]

def int_filter(l1):
    for v in l1:
        try:
            int(v)
            continue
        except ValueError:
            yield v
print(list(int_filter(l1)))


