# Leap year check ->

year = int(input("Enter Year :"))

if (year % 400) or (year%4==0 and year%100 !=0):
    print("Leap Year") 
else:
    print("Not Leap Year")
