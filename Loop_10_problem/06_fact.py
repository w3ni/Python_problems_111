# Factorial with while loop

num = int(input("Enter num : "))
factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print(factorial)