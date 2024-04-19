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

# WAP TO PRINT A FACTORIAL OF A NUMBER
n = 5
fact = 1
for i in range(1,n+1):
    fact = fact * i
print("Factorial of a num is ",fact)

#WAP to print factors of a number
n = 36
for i in range(1,n+1):
    if (n % i == 0):
        print(i,end="\t")
else:
    print("\nDone")