#Q1. Name the keyword which helps in writing code involving conditions.

#ANS:- 

#If / Else / Else If conditional statements are conditional statements that have more than one condition.  If the first condition is false, only then the second condition will be checked. If the second one is also false, then it will default to else or it will not do anything.


#Q2. Write the syntax of a simple if statement.

#ANS

#if (condition):
    #print("condition satisfied and print output")
#else:
    #print("print the oposite or give lines")
    



#Q3. Write a program to check whether a person is eligible for voting or not. (accept age from user)

#ANS

age=int(input ("enter you age :- "))
if age >=18 :
    print("you are eligible for vote ")
else:
    print("sorry, you are not eligible to vote because you are minor")


#Q4. What is the output of the given below program?

if 1 + 3 == 7:
    print("Hello")
else:
    print("Know Program")

#ANS

#OUTPUT   :-   Know program (else condition)



#Q5. Write a program to check whether a number entered by user is even or odd.

#ANS

num=int(input("enter the number to check even or odd : "))
if num%2==0:
    print("enter number is even")
else:
    print("enter number is odd")


#Q6. Python program to find the largest element among three Numbers ?
num1 = 10
num2 = 50
num3 = 15

#ANS

if (num1>num2) & (num1>num3):
    print("largest number is ", num1)
elif (num2>num1) & (num2> num3):
    print("largest number is ",num2)
else:
    print("largest number is ",num3)
    


#07. Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on

#ANS

x = int(input("Enter the number for which month and days you want to see : "))
if (x==1):
    print ("1 for January ")
    print("January have 31 days")
if (x==2):
    print("2 for Feburary")
    print(" Feburary have 28/29 days")
if (x==3):
    print("3 for March")
    print("March have 31 days ")
if (x==4):
    print("4 for April")
    print("March have 30 days")
if (x==5):
    print("5 for May")
    print("March have 31 days")
if (x==6):
    print("6 for June")
    print("june have 30 days")
if (x==7):
    print("7 for July")
    print("July have 31 days")
if (x==8):
    print("8 for August")
    print("August have 31 days")
if(x==9):
    print("9 for September")
    print("September have 30 days")
if(x==10):
    print("10 for October")
    print("October have 31 days")
if(x==11):
    print("11 for November")
    print("October have 30 days")
if(x==12):
    ("12 for December")
    print("October have 31 days")
if(x<1 or x>12):
    print("Invalid ")
