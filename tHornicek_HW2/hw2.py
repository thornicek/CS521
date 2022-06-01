#Tomas Hornicek, no collaborators,https://developer.mozilla.org/en-US/, https://www.w3schools.com/,no extension
import random

def is_leap(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 100 == 0) and (year % 400 == 0):
        return True
    else:
        return False
is_leap(2020)
is_leap(2001)
is_leap(2005)


def is_triangle(num):
   
    sum = 0
    n = 1
    while (sum <= num):
        sum = sum + n
        if (sum == num):
            return True
        n += 1
    return False


print(is_triangle(10))



def triangle_sum(lower_bound, upper_bound):
     tri_range = range(lower_bound,upper_bound+1)
     #print(tri_range)
     tri_list = list(tri_range)
     sum=0
     for i in tri_list:
         if is_triangle(i):
            #print(i)
            sum +=i
     return sum

print(triangle_sum(1,10))
print(triangle_sum(10,20))

def random_gen(n):
    random_list = list()
    for i in range(n):
        randomNumber = random.randint(1,9)
        random_list.append(randomNumber)
    return random_list
print(random_gen(100))

def bit_and(a,b):
    bit_list = list()
    a_list = list(a)
    b_list = list(b)
    length_a = len(a)
    length_b = len(b)
    if length_a > length_b:
        difference = length_a - length_b
        a_list = a_list[difference:]
    elif length_b > length_a:
        difference = length_b - length_a
        b_list = b_list[difference:]
    for i in range(len(a_list)):
        if a_list[i] == b_list[i] and a_list[i]=="1":
            bit_list.append(1)
        else:
            bit_list.append(0)
    sum = 0
    for index,value in enumerate(bit_list):
        if value == 1:
            powerOfTwo= len(bit_list) - index -1
            numberAdd = 2**powerOfTwo
            sum += numberAdd
    return sum
print(bit_and("101","110"))
print(bit_and("1011","10"))

def digit_sum(num):
    input_list = list(str(num))
    sum = 0
    for i in input_list:
        sum += int(i)
    if sum >= 10:
        return digit_sum(sum)
    else:
        return sum
print(digit_sum(129))










