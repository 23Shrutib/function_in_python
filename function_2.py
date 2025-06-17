#11-20: Conditional Statements

#program to check if a number is positive or negative
def pos_neg():
    n=int(input('enter the number to check if +ve or -ve '))

    if n>0:
        print('positive number!')
    else:
        print('negative number!')

#program to check if a number is even or odd
def even_odd():
    no=int(input('enter the number to check if even or odd '))

    if no%2==0:
        print('no. is even')
    else:
        print('no. is odd')


#program to check if a number is divisible by 5
def divisible_by_5():
    num=int(input('enter the number to check if divisible by 5 '))

    if num%5==0:
        print('divisible by 5')
    else:
        print('not divisible by 5')

#program to check if a number is divisible by both 3 and 5
def divisible():
    n=int(input('enter the number '))
    
    if n%3==0 and n%5==0:
        print('divisible by 3 & 5')
    else:
        print('not divisible by 3 & 5')

#program to check if a year is a leap year
def leap_year():
    
    year=int(input('enter year '))
    
    if year%4==0 and year%100==0 and year%400==0:
        print('leap year')
    else:
        if year%4==0 and year%100!=0:
            print('leap year')
        else:
            print('not leap year')

pos_neg()
even_odd()
divisible_by_5()
divisible()
leap year()
