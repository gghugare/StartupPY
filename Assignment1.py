name = str(input("Enter your Name : "))
roll = str(input("Enter your Roll Number : "))
Class = int(input("Enter your Standard : "))
Java = int(input("Enter your JAVA Marks : "))
C = int(input("Enter your C++ Marks : "))
PYTHON = float(input("Enter your PYTHON Marks : "))
RUBY = float(input("Enter your RUBY Marks : "))
SQL = int(input("Enter your SQL Marks : "))

Total = Java+C+PYTHON+RUBY+SQL
Percentage = (Total/500)*100

print("My name is : ",name)
print("My Roll Number is : ",roll)
print("My JAVA is : ",Java)
print("My C++ is : ",C)
print("My PYTHON is : ",PYTHON)
print("My RUBY is : ",RUBY)
print("My SQL is : ",SQL)
print("Total : ",Total)
print("Percentage is : ",Percentage)