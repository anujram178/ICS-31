# Ramaswamy, Anuj

# Problem 1
r = float(input("Enter a radius: "))
h = float(input("Enter a height: "))
import math
volume = math.pi*r**2*h
print(volume)

# Problem 2
F = input("Enter a first name: ")
L = input("Enter a last name: ")
i = len(F)+1
revised_i = F.ljust(i)
print(revised_i*2+L*3)

# Problem 3
= input("Enter the first sequence of numbers separated by commas: ")
b = input("Enter the second sequence of numbers separated by commas: ")
a = a.split(',')
for i in range(len(a)):
    a[i] = int(a[i])
b = b.split(',')
for i in range(len(b)):
    b[i] = int(b[i])
lst=[]
for i in a:
    for j in b:
        lst.append((i,j))
print(lst)

# Problem 4
i = float(input("Enter a number: "))
a = (abs(i)**(1/3))
print("result:", a)

# Problem 5
notPrime=False
l=[]
l5=[]
for a in range(2,251):
    for b in range(2,int (a**0.5)+1):
        if a%b==0:
            notPrime=True
            break
    if notPrime==False:
        l.append(a)
    else:
        notPrime=False
for a in l:
    s=0
    a2=a
    while a>0:
        s=s+(a%10)
        a=a/10
    if s>=6:
        l5.append(a2)
print(l5)

# Problem 6
import random
r = random.randint(0,101)
i=-1
while i != r:
    i = int(input("enter random number"))
    if i > r:
        print("Number is less than ", i)
    if i < r:
        print("Number is greater than ", i)
if i == r:
    print("congratulations! you are correct")

    
# Problem 7
11+13+15+17+19
statistics.stdev([75,83,47,29,96])
66**(1/4)
0.5*40*(10**2)

# Problem 8
test_scores = "2 5 6 9 3 8 2 6 5 9 5 6 6 2 9 0 9 8 8 7"
print(test_scores[2])
print(test_scores[26])
print(test_scores[14]) + print(test_scores[16])
print(test-scores[36]) - print(test_scores[4])

# Problem 9
s = "computerscience"
s[-1] == 'b'
s[0] == 'c'
s.count('e') == 3
len(s) == 16

# Problem 10
type(2.0*6) == int
len(s*3) == 15
(20%5) <= 2
type(62) == float

# Problem 11
s = 'abcdefghijklmnopqrstuvwxyz'
print(s[7]+s[0]+(s[-9]*2)+s[8]+s[-8])
print(s[11]+s[0]+s[1])
print(s[13]+s[4]+s[-4])
print(s[12]*3+s[-2]+s[-4])
