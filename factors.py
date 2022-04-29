# int = input("Enter your name: ")    
# print(f"Hello {int}")
# int = input ("Eneter your last name: ")
# int2= input ("Enter these :")
# print(f"Kaise ho {int} tum ho {int2}")

# Python program to
# print current date

#from datetime import date

# calling the today
# function of date class
# today = date.today()
# today.__format__('date')
# print("Today's date is", today)

# Printing date's components
#print("Date ", today.day, today.month, today.year)


# def factorial(n):
#     fact = 1
#     while(n>0):
#         fact = fact * n
#         n = n-1
#     return fact   


# t = int(input('Enter no. of testcases: '))
# while (t>0):
#     n = int(input('Enter n: '))
#     res = factorial(n)
#     print(f"The Factorial is:{res} \n")
#     t = t-1
def factorial(n):
    result = 1
    for i in range (2,n+1):
        result = i * result
    return result 

print (factorial (4))


