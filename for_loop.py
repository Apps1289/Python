# >> Let's learn here about for loop

list1= ["abi",4,3,10,'rakesh']

for sth in list1:
    print(sth)
else:
    print("Done")

for ntg in "AbhiUranw":
    print(ntg)
else:
    print("Nice!")

# Accesing all the user taken elements from the list
list2 = []
for i in range(5):
    list2.append(i)
print(list2)
for sth in list2:
    print(sth)
else:
    print("Successfull!")
for ntg in list2:
    if (ntg == 4):
        print("Found it!!")
else:
    print("Done")