list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80] 
 
new = []#output list
for i in list: 
    n = list.count(i)#check the element occurence
    if n > 1:#condition to check if element is occured more thin 1, idd it to the new list     
 
        if new.count(i) == 0:  #condition to check
 
            new.append(i)
 
print(new)