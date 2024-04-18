#string
str = "I am a boy."
print(len(str))
print(str[::-1])
print(str.endswith("oy"))
print(str.find("a"))
print(str.count("a"))




# lets have a glimpse about list
# lists are ordered and mutable

l1 = [1,2,10,9]
# can have any datatypes
print(l1)
print(len(l1))
# l1[1] = "raja"
print(l1.append(56)) # add element at last
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
l1.insert(1,"ahi")
print(l1)


