# let's learn about tuple
# tuple: immutable and ordered

tup1=(1,2,6,3,'prashna')
print(tup1)
print(len(tup1))
# tup1[1] = 'diwass' >> not allowed in tuple since they are immutable
print(tup1[3])
print(tup1.index(3))
print(tup1.count(6))

# WAP TO ASK USER TO ENTER THEIR FAV MOVIES AND PRINT THE LIST OF THE MOVIES

list1=[]
movie1=input("Enter 1st movie:")
movie2=input("Enter 2st movie:")
movie3=input("Enter 3st movie:")
list1.append(movie1)
list1.append(movie2)
list1.append(movie3)
print(list1)

# WAP TO Check if list contains PALINDROM number or not
sth = [1,4,3,2,1]
print(sth)
rev = sth[::-1]
print(rev)
if(sth == rev):
    print("Palindrom")
else:
    print("Not a Palindrom")

