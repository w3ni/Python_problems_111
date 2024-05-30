# Password check , weak / medium / strong

passwd = input("Enter your pass : ")

if len(passwd) <6:
    st = "Weak"
elif len(passwd) <=10:
    st = "Medium"
else:
    st = "Strong"

print("Pass strength is:", st)
