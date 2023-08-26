'''-- User input section
Enter Product 1 -
Samosa
Do you Want to add more [Y/N]
Y
Enter Product 2 -
Kachori
Do you Want to add more [Y/N]
Y
Enter Product 3 -
Fafda
Do you Want to add more [Y/N]
Y
Enter Product 4 -
Jalebi
Do you Want to add more [Y/N]
N
Enter Samosa Price :
300/-
Enter Kachori Price :
100/-
Enter Fafda Price :
100/-
Enter Jalebi Price :
200/-

Do You Want to add GST [Y/N]
[note : if user select `N` Print bill without GST]
[Note User select yes `Y`]
Enter GST % = 18
-------Out put -------

1. Samosa = 300/-
2. Kachori = 100/-
3. Fafda = 100/-
4. Jalebi = 200/-
-------------------
Total = 700
GST = 18%
-------------------
Final Total = 826/-
-------------------'''

Y = "Y"
N = "N"
product = str(input("Enter Product 1"))
print("Your order is ",product)
q1 = str(input("Do you Want to add more [Y/N]  "))

if q1 == Y:
    product = str(input("Enter Product 2"))
    print("Your order is ",product)
    q1 = str(input("Do you Want to add more [Y/N]  "))  
elif q1 == Y:
    product = str(input("Enter Product 3"))
    print("Your order is ",product)
    q1 = str(input("Do you Want to add more [Y/N]  "))
elif q1 == Y:
    product = str(input("Enter Product 4"))
    print("Your order is ",product)
    q1 = str(input("Do you Want to add more [Y/N]  "))