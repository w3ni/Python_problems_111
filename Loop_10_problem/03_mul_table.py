# Multiply table skip 5th num

num = int(input("Enter num : "))

for i in range(1,11):
    if i == 5:
        continue
    print(num, 'X' , i , '=' , num*i)