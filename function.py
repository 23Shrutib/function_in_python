#FUNCTION:-

'''
def even_odd():
    n=int(input("enter number "))
    if n%2==0:
        print("even")
    else:
        print("odd")

def for_loop():
    for i in range(1,11,1):
        print(i)
'''

'''
#program to print "Hello, World!"
def hello_world():
    print("hello world")
'''
'''
#program to take a user's name as input and greet them
def greet():
    name=input('enter name ')
    print(f'Greetings {name}')

'''
'''
#program to add two numbers provided by the user
def add():
    num1=int(input('enter num1 '))
    num2=int(input('enter num2 '))
    print('Addition is ',num1+num2)


#program to subtract two numbers
def sub():
    a=100
    b=50
    print('subtraction is ',a-b)


#program to multiply two numbers
def multiply():
    m=10
    n=4
    print('Multiplication is',m-n)


#program to find the square of a number
def square():
    numb=int(input('enter a number '))
    print('Square of number is ',numb**2)
'''


'''
#program to swap two numbers using a third variable
def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function and store the returned values
num1, num2 = swap_numbers(num1, num2)

# Print the swapped numbers
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)

'''
'''
even_odd()
for_loop()
hello_world()
greet()
add()
sub()
multiply()
square()
'''

###############################################30 May
#FUNCTION ARGUMENTS:-

'''
#1]positional argument   #most of the time positional argument is used
def addition(a,b):
    print(a+b)

addition(10,20) #arguments
addition(15,25)
'''

'''
#2]keyword arguments
def addition(a,b):
    print(a+b)

addition(a=10,b=20)
'''

'''
#3]default arguments:-
def addition(a,b=20):
    print(a+b)

addition(10)
addition(15)
'''

'''
#4]variable length arguments:-
def addition(*a):  #tuple of a
    for i in a:
        print(i)

    print(a[0]+a[1])

addition(10,14,3,22,5,7,9)
'''

'''
#5]keyword variable length arguments:-
def addition(**d):  #dict
    for i in d:
        print(d[i])

    print(d['a']+d['b'])

addition(a=10,b=14,c=3,d=22,e=5,f=7,g=9)
'''



#function scope
'''
x=100 #global scope

def demo():
    a=10    #local scope
    print(a)

demo()
print(x)
'''


'''
a=11  #global variable

def demo():
    a=10   #local variable
    print(a)

demo()
print(a)
'''



'''
#global keyword

a=10

def demo():
    a=11
    print(a)

demo()
print(a)
'''


'''
#practice question no.1 ??????????
x=10

def demo():
    z=20
    if x!=z:
        print(z)
    else:
        global x
        x=54

demo()
print(x)
'''


'''
#practice ques no.2
z=14

def sample():
    global z
    x=42
    z=23
    print(z)
    if z>=x:
        x=14
        print(x)
    else:
        x=14
        print(x)

sample()
print(z)
'''




'''
#lambda function

demo=lambda x, y: print(x+y)

demo(10,20)
'''
