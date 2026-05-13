class phone:
    def fun1(self):
        print("Talk with friends...")

class smart_phone(phone):
    def fun1(self):
        super().fun1()
        print("Talk and chat with your friends..")
sm = smart_phone()
sm.fun1()

from abc import ABC,abstractmethod
class ebook(ABC):#abstract class
    @abstractmethod
    def source(self):
        print("Book Name : Learn Python")
        print("Author Name : Pradeepa")
        print("Sensitive data")
    def java_source(self):
        print("Book Name : Learn java")
        print("Author Name : praveen")
        print("Sensitive data")

class vendor(ebook):
    def source(self):
        print("Book Name : Learn Python")
        print("Author Name : Naga raj")

v = vendor()
v.source()
v.java_source()

class ac_details:
    name = "Praveen Kumar"
    _ac_no = 123456786
    __pin = None
    def setPin(self,p):
        self.__pin = p
    def getName(self):
        return self.name
class bank(ac_details):
    _ac_no = 876543225
    __pin = None
    def fun1(self):
        print(self.name)
        print(self.__pin)
ac = ac_details()
print(ac.name)
print(ac.__pin)
b = bank()
b.fun1()
b.setPin(3456)

name = b.getName()
print("AC Holder Name :",name)

'''
class Laptop:
    def __init__(self, b, m, p):
        self.brand = b
        self.model = m
        self.price = p

    def display(self):
        print(self.brand)
        print(self.model)
        print(self.price)

l1 = Laptop("Lenovo", "CPH21", 34000)
l2 = Laptop("Dell", "CPH22", 38000)
print("Display laptop Details")
l1.display()
print("====================")
l2.display()


class Student:
    def __init__(self, i, n, m):
        self.id = i
        self.name = n
        self.mark = m

    def display(self):
        print(self.id)
        print(self.name)
        print(self.mark)


s1 = Laptop("001", "Bharathi", 450)
s2 = Laptop("002", "Brindha", 380)
print("Display Student Details")
s1.display()
print("====================")
s2.display()

class Fan:
    brand = None
    model = None
    price = None

    def switch_on(self):
        print(self.brand,"Button helps to fan on/off.....")
        print("END".center(30, '*'))

f1 = Fan()

f1.brand = "sky"
f1.model = "2ert90"
f1.price = 1500

print("fan Brand:", f1.brand)
print("fan model:", f1.model)
print("fan price:", f1.price)
f1.switch_on()


class Book_info:#super class
    name = "Learn Artificial inteigence"
    def fun1(self):
        print(f"Book Name : {self.name}")

class Author(Book_info):#sub-class
    au_name = "Bharathi"
    def fun2(self):
        print(f"Author Name : {self.au_name}")


class Book_price(Author):
    def fun3(self):
        print("Book Price Rs : 500")

class Book_genre(Book_price):
    def fun4(self):
        print("Book Genre : Tech Learning")

g = Book_genre()
g.fun4()
g.fun3()
g.fun2()
g.fun1()

class bike():
    def bike_ride(self):
        print("bike is ride on the road")
b = bike()

b.bike_ride()

class Mobile():
    def call(self):
        print("Mobile is calling.......")
m1 = Mobile()

m1.call()
'''

class employee():
    emp_id = "001"
    emp_name = "Bharathi"
    emp_salary = 20000
    def fun1(self):

        print("Employee Name is:",self.emp_name)
        print("Employee id is:",self.emp_id )
        print("Employee salary is:",self.emp_salary)
e = employee()
e.fun1()

class hospital():
    hos_loc = "Chennai"
    doc_name = "Bharathi"
    hos_name = "Amirtha"
    def fun1(self):

        print("Hospital Name is:",self.hos_name)
        print("Hospital location is:",self.hos_loc )
        print("Doctor Name:",self.doc_name)
h = hospital()
h.fun1()





