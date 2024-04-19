# > lets dig into the function

def sum_of(a,b):
    sum = a+b
    # print(sum)
    return sum
output = sum_of(4,5)
print(output)
sum_of(4,9)
sum_of(4,7)

# average of three numbers
def avg_of_num(a,b,c):
    avg = (a+b+c)/3
    print(avg)
    return avg
avg_of_num(4,5,6)

#factorial of a number using function

def fact_of_num(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print(fact)
fact_of_num(5)
    

# > 
cities = ["Ithari", "Biratnagar","Kathmandu", "Lalitput"]

def name_cities(list1):
    print(len(list1))
name_cities(cities)

def access_cities(list1):
    for el in range(len(list1)):
        print(list1[el],end="\n")
access_cities(cities)

# PRACTISE QUESTONS
#> RECURSION

def recur(n):
    if(n==0):
        return
    print(n)
    recur(n-1)
recur(5)

#> FACTORIAL
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# print sum of natural number using recursion

def sum_of_natural(n):
    if(n==0):
        return 0
    else:
        return n + sum_of_natural(n-1)
print(sum_of_natural(5))

