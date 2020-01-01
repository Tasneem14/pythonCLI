

import math
import cmath
import statistics


def add(x,y):
    return x+y

def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def devide(x,y):
    return x/y
def idv (x,y):
    return x//y
def fact(x):
    sum=1
    for i in range(1,x+1):
        sum=sum*i
    return sum
def pow(x,y):
    return x**y
def sqrt(x):
    return(math.sqrt(x))

def Fibonacci(x):

        if x < 0:
            print("Incorrect input")
            # First Fibonacci number is 0
        elif x == 1:
            return 0
        # Second Fibonacci number is 1
        elif x == 2:
            return 1
        else:
            return Fibonacci(x - 1) + Fibonacci(x - 2)

            # Driver Program



def prime(x):

  answer="yes"
  for i in range(2,x):
    if x%i==0:
        answer="no"

  return(answer)
def sums(x):
    y=0
    for i in range(1,x+1):
        y=i+y
    return(y)
def squareSum(x):
    y=0
    for i in range (1,x+1):
        y=(i**2)+y
    return(y)
def evenSquareSum(x):
    y=0
    for i in range(1,x+1):
        if i%2==0:
            y=(i**2)+y
    return(y)
def oddSquareSum(x):
    y=0
    for i in range(1,x+1):
        if i%2!=0:
            y=(i**2)+y
    return(y)
def quadratic(a,b,c):


     x1=(-b+ cmath.sqrt((b**2)-(4*(a*c))))/(2*a)
     x2=(-b- cmath.sqrt((b**2)-(4*(a*c))))/(2*a)

     return(x1,x2)
def count(x):
    y=0
    while x>0:
        x=x//10
        y=y+1

    return(y)
def counte (x):
    y=0

    for i in str(x):
        if int(i)%2==0:

            y=y+1
    return(y)
def counto(x):
    y=0
    for i in str(x):
        if int(i)%2:
          y=y+1

    return(y)
def pow(x):
    return(x**2)
def armstrong(x):

     sum=0
     y=x

     while y>0:
         z=y%10
         sum=sum+z**3
         y//=10
         if x==sum:
             answer="yes"
         else:
             answer="no"


     return answer

def dip(x):

   return( (x**x)**x)**x
def multisum(x,y):
    i=0
    z=0
    while z<y:
        i=i+x
        z=z+1
    return i
def rev_list(x):

   return x[::-1]
def increasing_array(l):

    if all(x < y for x, y in zip(l, l[1:])):
        answer="yes"
    else:
        answer="no"
    return answer
def decreasing_array(l):
    if all(x > y for x, y in zip(l, l[1:])):
        answer = "yes"
    else:
        answer = "no"
    return answer
def monotonic(l):
    if all(x < y for x, y in zip(l, l[1:])):
        answer = "yes"
    elif all(x > y for x, y in zip(l, l[1:])):
        answer = "yes"
    else:
        answer="no"
    return answer
def maximum(x):
    return max(x)
def minimum(x):
    return min(x)
def count_prime(x):
    list=[]
    for z in x:

            answer = "yes"
            for i in range(2, z):
                if z % i == 0:
                    answer = "no"
            if answer=="yes":


              list.append(z)

    return len(list)
def rep_fact(x):
    list=[]
    for z in x:
     sum=1
    for i in range(1,z+1):
        sum=sum*i
        list.append(sum)
    return(list)
def average(x):
    y=0
    list=[]
    for i in x:
        y=y+i
        list.append(i)
    return y//len(list)
def mode(x):
    return (statistics.mode(x))
def pyramide(x):
     answer="yes"
     for i in range (0,len(x)//2):
       if x[i]!=x[len(x)-i-1]:
         answer="no"
     return answer
def panagram(x):

    for i in x:
        if (i>="A" and i<="Z")or(i>="a" and i<="z"):
            answer="yes"
        else:
            answer="no"
    return answer
def palindrome(x):
    answer = "yes"
    for i in range(0, len(x) // 2):
        if x[i] != x[len(x) - i - 1]:
            answer = "no"
    return answer


def z(x):
    for i in range(x):
        print(" ")
        if(i==0 or i==x-1):
            for j in range(1,x+1):
                print(j,end=" ")
        else:
            ii=x-i
            for j in range(1,x+1):
                if(j==ii):
                    print(ii,end=" ")
                else:
                    print(" ",end=" ")
    return print
def staircase(x):
    k = 0

    for i in range(1, x + 1):
        for space in range(1, (x - i) + 1):
            print(end="  ")
        while k != (2 * i - 1):
            print("* ", end="")
            k = k + 1
        k = 0
        print()
def isp(x):
    for i in range(0, x):
        for j in range(x, i, -1):
            print("* ", end="")
        print()


def arrow(x):

    for i in range(x):
        print(' '*1,end=" ")
        print('*'*(i+1))
    for i in range (x-1,0,-1):
        print(' '*(i-1),end=" ")
        print('*'*(i))
def count_matching(x,y):
    z=[]
    for i in set(x):
      for j in set(y):
        if i==j:
          z.append(i)

    return len(z)
#def count_matching(test1,test2):
    common = 0

    #if len(test1) < len(test2):
        #for letter1 in test1:
            #if letter1 in test2:
                #letter1=1
                #common=common+1

    #else:
        #for letter2 in test2:
           # if letter2 in test1:
               # letter2=1
               # common=common+1
    #return common













def main():
    while(True):

      i= (input())
      if i=="hi":
        print("hi there")

      elif (i == "sum"):
        x = eval(input("Enter frst num "))
        y = eval(input("Enter second num "))
        print(x, "+", y, "=", add(x, y))
      elif i == "sub":
        x = eval(input("Enter frst num "))
        y = eval(input("Enter second num "))
        print(x, "-", y, "=", sub(x, y))
      elif i == "multiply":
        x = eval(input("Enter frst num "))
        y = eval(input("Enter second num "))
        print(x, "*", y, "=", multiply(x, y))
      elif i == "devide":
        x = eval(input("Enter frst num "))
        y = eval(input("Enter second num "))
        print(x, "//", y, "=", devide(x, y))
      elif i == "idv":
          x = eval(input("Enter frst num "))
          y = eval(input("Enter second num "))
          print(x,"/",y,"=",idv(x,y))
      elif i =="fact":
          x = eval(input("Enter frst num  "))
          print("fact","=",fact(x))
      elif i =="sqrt":
          x = eval(input("Enter a num"))
          print("square root of",x,"=",sqrt(x))
      elif i =="fibonacci":
          x = eval(input("Enter a num "))
          print(Fibonacci(x))
      elif i =="prime":
          x = eval(input("Enter a num "))
          print(prime(x))
      elif i =="sums":
          x = eval(input("Enter a num "))
          print(sums(x))
      elif i=="squareSum":
          x = eval(input("Enter a num "))
          print(squareSum(x))
      elif i=="evenSquareSum":
          x = eval(input("Enter a num "))
          print(evenSquareSum(x))
      elif i=="oddSquareSum":
          x = eval(input("Enter a num "))
          print(oddSquareSum(x))
      elif i=="armStrong?":
          x = eval(input("Enter a num "))
          print(armstrong(x))
      elif i=="quadratic":

          a= eval(input("Enter first num "))
          b= eval(input("Enter second num "))
          c= eval(input("Enter third num "))
          print(quadratic(a,b,c))
      elif i=="count":
          x=eval(input("Enter a num "))
          print("number of digits","=",count(x))
      elif i=="counte":
          x = eval(input("Enter a num "))
          print("number of even digits","=",counte(x))
      elif i=="counto":
          x = eval(input("Enter a num "))
          print("number of odd digits","=",counto(x))
      elif i=="power":
          x = eval(input("Enter a num "))
          print("=",pow(x))
      elif i=="dip":
          x = eval(input("Enter a num "))
          print("=",dip(x))
      elif i=="multisum":
          x = eval(input("Enter a num "))
          y = eval(input("Enter a num "))
          print(x,"*",y,"=",multisum(x,y))
      elif i=="rotate":
          x = eval(input("Enter a list "))
          print(rev_list(x))
      elif i=="inc?":
          l = eval(input("Enter a list "))
          print(increasing_array(l))
      elif i=="dec?":
          l = eval(input("Enter a list "))
          print(decreasing_array(l))
      elif i=="monotonic?":
          l = eval(input("Enter a list "))
          print(monotonic(l))
      elif i=="max":
          x = eval(input("Enter a list "))
          print("the maximum num is ",maximum(x))
      elif i=="min":
          x = eval(input("Enter a list "))
          print("the minimum num is ",minimum(x))
      elif i=="countPrime":
          x = eval(input("Enter a list "))
          print ("the num of prime num is ",count_prime(x))
      elif i=="repFact":
          x= eval(input("Enter the list "))
          print(rep_fact(x))
      elif i=="average":
          x = eval(input("Enter the list "))
          print("the average","=",average(x))
      elif i=="mode":
          x = eval(input("Enter the list "))
          print("the mode","=",mode(x))
      elif i=="pry?":
          x = eval(input("Enter the list "))
          print(pyramide(x))
      elif i=="panagram":
          x = input("Enter string ")
          print(panagram(x))
      elif i=="palindrome":
          x = input("Enter string ")
          print(palindrome(x))
      elif i=="countmatching":
          x = input("Enter first string ")
          y = input("Enter second string ")
          print(count_matching(x,y))
      elif i=="Zpattern":
          n= eval(input("Enter pattern size "))
          print(z(n))
      elif i=="staircase":
         x= eval(input("Enter patt4\85/ern size "))
         print(staircase(x))
      elif i=="isp":
          x = eval(input("Enter pattern size "))
          print(isp(x))
      elif i=="arrow":
          x=eval(input("Enter pattern siza "))
          print(arrow(x))
      elif i =="bye":
          print("bye")
          print("python CLI will shut down ..")
      else:
        print("what?")

main()




















