*#if a month season*

month = input("Enter month name: ")

if["december", "january", "february"]:
    print("Winter Season")
elif["march", "april", "may"]:
    print("Summer Season")
elif["june", "july", "august"]:
    print("Monsoon Season")
elif["september", "october", "november"]:
    print("Autumn Season")
else:
    print("Invalid")

*#find the hello*

print("hello")
p=int(input("enterthe value:"))
if p>10:
    print("Hello Bhrathi")
else:
    print("Bye")

*#find the max and min of three  numbers*

a = 100
b = 450
c = 390

maximum = max(a, b, c)
minimum = min(a, b, c)

print(f"The maximum number is:",maximum)
print(f"The minimum number is:",minimum)

*#find the students leap year or not* 

year =int(input("Enter the year:"))
          
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print("this is a leap year")
else:
   print("this is not a leap year")


*#find the vowels and constants*

v = input("Enter a letter (A to Z): ")

if v.upper() in ["A", "E", "I", "O", "U"]:
    print("It is a vowel:", v)
else:
    print("It is a consonant")


*#find the students pass or fail*

avg =45
avg =int(input("Enter the Student Mark:"))
if  avg >35:
 print("Student Pass")
else:
  print("Fail")

*#find the value of odd or even*

m=int(input("Enter the Number:"))
if (m%2)== 0:
       print("m is a Even")
else:
     print("m is Odd")

*#find the students grade*

avg =60
avg =int(input("Enter the Student Mark:"))
if  avg >=90 and avg >=80 :
 print("Student get A+ grade")
elif avg >80 and avg >=75:
  print("Student get A grade")
elif avg >75 and avg >=70:
  print("Student get B+ grade")
elif avg >70 and avg >= 65:
  print("Student get B grade")
elif avg >65 and avg>60:
  print("Student get C grade")
else:
  print("Fail")


*#find the value of positive or negative value*

num = int(input("Enter number: "))

if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

#find the value of m and n
m = int(input("Enter m Value :"))
n = int(input("Enter n Value :"))
if m>n:
    print("Quatient :", m//n)
    
    print("Remainder :", m%n)
else:
    print("n greater than m..")


*#find the value of month day count*
    
month = input("Enter month: ").lower()
year = int(input("Enter year: "))

if month == "february":
    if (year % 4 == 0):
        print("29 days")
    else:
        print("28 days")

elif ["april", "june", "september", "november"]:
    print("30 days")

elif ["january", "march", "may", "july", "august", "october", "december"]:
    print("31 days")

else:
    print("Invalid month")


*#find the value of odd or even*

    m=int(input("Enter the Number:"))
    if (m%2)== 0:
       print("m is a odd number")
    else:
     print("m is not even number")

     *#find age eligible or not*

p=int(input("Enter the Age:"))
if p>18:
 print("Age is Eligible for Police")
else:
 print("Not Eligible for Police")


*#find the Employee Bonus to salary*

salary=float(input("Enter the salary:"))
bonus_percent =float(input("Enter the Bonus Percentage:"))            
bonus = (salary * bonus_percent) / 100
total_salary = salary + bonus

print("Get the Bonus Value",bonus)
print("Get the Total Salary", total_salary)                


*#find the Temperature of celcius water boiled or not*

temp=int(input("Enter the emperature Value:"))
if temp>=100:
    print("Water Boiled")

else:
    print("Not Boiled Water")
