#problem 1
print("Hello World")

#Mohammed adnan Khan
# Feb 5 2023
# prints hello world

#problem 2

name= input("Please Enter Your name: ")
print("Good Morning ",name,"Welcome to CSS225")

#Mohammed Adnan Khan
# feb 5 2023
# greeting the user

#problem 3
name= input("Please Enter Your name: ")
instructor= 'Zoe Likoudis'
print("Good Morning ",name,"and",instructor,"Welcome to CSS225")

#Mohammed Adnan Khan
# feb 5 2023
# greeting the user and the instructor

#problem 4

rad= int(input("Enter the area of the circle"))
area= 3.14159 * rad * rad
print("The area of the circle is  ",area)




#Mohammed Adnan Khan
# feb 5 2023
# finding the area of the circle

#problem 5
miles= float(input("Enter the number of miles driven"))
gallon= float(input("Enter the amount gallons used"))
mpg= miles / gallon
print("The car provides",mpg,"mpg")


#Mohammed Adnan Khan
# feb 5 2023
# Calculating miles per gallon

#problem 6

F= int(input("Enter Fahrenheit"))
C= (F - 32) * 5/9
print( F,"Fahrenheit degree is",round(C),"Celsius degree")
       
#Mohammed Adnan Khan
# Feb 5 2023
# converts Fahreniet in to Celsius

#problem 7
lists= ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
day= int(input("Enter the starting number: "))
stay= int(input("Lenght of your stay: "))
value= 0

while value != stay:
    day= day + 1
    value += 1
    if day > 6:
        day= 0
print(lists[day],"day" ,day)

#Mohammed Adnan Khan
# Feb 5 2023
# program  asks for the starting day number, and the length of your stay, andit will tell you the number of day of the week you will return on.
























