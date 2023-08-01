Year1=int(input("My birth year is : "))
Month1=int(input("My birth month is : "))
Day1=int(input("My birth day is : "))

CurrentYear2=int(input("Enter your Current Year : "))
CurrentMonth2=int(input("Enter your Current Month : "))
CurrentDay2=int(input("Enter your Current Day : "))

print("My birth year is  : ",Year1)
print("My birth month is : ",Month1)
print("My birth day is : ",Day1)

print("Current year is : ",CurrentYear2)
print("Current month : ",CurrentMonth2)
print("Current day is : ",CurrentDay2)

print(CurrentYear2-Year1, 'year')

sum = CurrentMonth2-Month1
sum1 = (12-Month1)+(CurrentMonth2)
sum2 = Day1-CurrentDay2
sum3 = ((31-Day1)+CurrentDay2)

if Month1<CurrentMonth2:
   print(sum,'months')
else : 
    Month1>CurrentMonth2
    print(sum1,'months')

if Day1<CurrentDay2:
   print(sum2,'days')
else : 
    Day1>CurrentDay2
    print(sum3,'days')