#1
class counter:
    # counter=1
    def __init__(self,counter):
        self.counter=counter
    def inc(self):
        self.counter= (self.counter + 1)
        return self.counter
    def dec(self):
        self.counter= (self.counter - 1)
        return self.counter
    def getvalues(self):
        return self.counter
v=counter(1)
print(v.getvalues())
v.inc()
print(v.inc())
v.dec()
print(v.dec())





#2
from datetime import datetime
tdate= datetime.now()
print("Today is: ", tdate.strftime("%m-%d-%Y"))




#3
class person:
    def __init__(self,name, last_name, birth_date):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
    def get_age(self):
        pass
    def can_vote(self,age):
        if (age >= 18):
            return "Eligible to vote"
        else:
            return "Not Eligible to vote"
x=person("Bob","Dylan","May 24, 1941")
print("Name: ",x.name)
print("Last Name: ",x.last_name)
print("Brith date: ",x.birth_date)
print(x.can_vote(17))




#4
def maxnum(x,y):
    if (x>y):
        print(x,"= x is greater than y =",y)
    else:
        print(y,"= y is greater than x =",x)
maxnum(3,2)




#5
def fizz_buzz(num):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 5==0 and num % 3==0:
        print("FizzBuzz")
    else:
        print(num)
fizz_buzz(5)




#6
def spm(speed):
    if speed<70:
        print("OK")
    if speed>70:
        pts = (speed - 70) // 5
        print('pts = {}'.format(pts))
        if pts >= 12:
            print("License suspended")
spm(140)




#7
def shownumbers(limit):
    for i in range(0, limit):
        if i==0:
            print(i,end=" ")
            print("EVEN")
        elif i%2==0:
            print(i,end=" ")
            print("EVEN")
        else:
            print(i,end=" ")
            print("ODD")
shownumbers(10)




#8
def sum(limit): 
    sum = 0
    for i in range(0,limit+1):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
        i = i + 1
    return sum
x = int(input("Enter limit number: "))
print(sum(x))




#9
def show_stars(rows):
    for i in range(0, rows):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")
show_stars(5)




#10
def Prime(lim):
    if(lim==1 or lim==0):
        return "Neither prime nor consonant number"
    for i in range(2,lim+1):   
        if(lim%i==0):
            return False
        return True
lim = 100
for i in range(1,lim+1):
  if(Prime(i)):
    print(i,end=" ")

def age(a):
    if a>=21:
        print ("True")
    else:
        print ("False")
age(21)