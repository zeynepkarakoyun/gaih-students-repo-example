list1= [1,3,5,7]
list2= [2,4,6,8]
list1.extend(list2)
print(list1)
#i am not sure if you want the numbers in ascending sort but in case of you do the codes that i'd use are down below.
list1.sort()
print(list1)
newList = [i * 2 for i in list1]
print(newList)

for i in newList:
    print(f"{type(i)}")