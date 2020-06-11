# Ramaswamy, Anuj
# Problem 1
import math
def specialPrime(x):
    if x == 1 or x**2 > 999999:
        return False
    elif x!= 1:
        factors = 0
        for y in range(1,int(x)):
            if x%y == 0: #if x is divisible by y
                factors += 1
                if factors == 2: #the number has a factor other than one and itself
                    return False
    if factors == 1:
        return True 
num = int(input("enter a number: "))
f = specialPrime(num)
print(f)

# Problem 2
import random
def hangman():
    strikecount = 0
    win = 0
    guesses = set()
    myList = ["dog","cat","mom","dad","lizard"]
    secretWord = random.choice(myList)
    secretWordSet = set(secretWord)
    while strikecount<8 and win==0:
        guess = input("Guess a letter: ")
        if guess in secretWord:
            guesses.add(guess)
            print (guess + " is in the word")
            print ("strike count = ", strikecount)
            if guesses == secretWordSet:
                print("congrats, you won the game")
                win = 1
        elif guess not in secretWord:
            print (guess+ " is not in the word")
            strikecount += 1
            print ("strike count= ", strikecount)
    if strikecount>= 8:
        print("sorry you lost")
hangman()
        
#Problem 3
def leastcm(x,y):
    minimum = min(x,y)
    maximum = (x*y)+1 #for negative numbers, lcm is not possible
    if x == 0 or y == 0:
        return 0
    for multiple in range(minimum, maximum):
        if multiple % x == 0 and multiple % y == 0:
            return multiple
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
f = leastcm(num1,num2)
print("least common multiple is",f)

#Problem 4
def listmult(x):
    x.sort()
    l = len(x)
    if l%2 == 0:
        median = (x[(l//2)-1] + x[l//2])*0.5
    if l%2 != 0:
        median = x[(l-1)//2]
    for i in range(l):
        x[i] = x[i] + median
    return x
myList = input("enter a list of five or less numbers seperated by commas: ").split(',')
for j in range(len(myList)):
    myList[j] = int(myList[j])
f = listmult(myList)
print(f)

    
        
#Problem 5
def newAvg(myList):
    small = min(myList)
    s = sum(myList)
    s = s-small
    newavg = s/(len(myList)-1)
    return newavg
lst = input("Enter list of grades seperated by commas: ").split(',')
for i in range(len(lst)):
    lst[i] = int(lst[i])
new = newAvg(lst)
print("The new average of the list of grades: ", new)



#Problem 6
def atStartEnd(small,big):
    s = len(small)
    return small == big[:s] or small == big[-s:]

string1 = input("enter the first string: ")
string2 = input("enter the second string: ")
if len(string1) < len(string2):
    f = atStartEnd(string1,string2)
else:
    f = atStartEnd(string2,string1)
print(f)

#Problem 7
word = "ics"
def findics(x):
    if word == x[:3] or word == x[1:4]:
        return False
    elif word in x:
        return True
    else:
        return False
yourWord = input("enter a word: ")
if len(yourWord) <= len(word)+1:
    f = False
f = findics(yourWord)
print(f)

#Problem 8
import math
def Fcutoff(x):
    for i in range(len(x)):
        x.sort()
        cutoff = x[math.ceil(len(x)*0.3)]
    return str(cutoff)+ " is the cutoff grade for an D"
myList = input("enter a list of grades seperated by commas: ").split(',')
for i in range(len(myList)):
    myList[i] = int(myList[i])
f = Fcutoff(myList)
print(f)


#Problem 9
lst = [1,2,2,5]
def pastaCalc(m,t,o,p):
    _m = m
    _t = t//2
    _o = o//2
    _p = p//5
    return min(_m,_t,_o,_p)
mushrooms = int(input("enter the number of mushrooms: "))
tomatoes = int(input("enter the number of tomatoes: "))
tablespoons = int(input("enter the number of tablespoons of olive oil: "))
pasta = int(input("enter the number of batches of pasta: "))
f = pastaCalc(mushrooms,tomatoes,tablespoons,pasta)
print(f"you can make {f} bowl(s) of pasta")











