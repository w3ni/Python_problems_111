# Check non repeated word

str = input("Enter your word : ")

for char in str:
    print(char)
    if str.count(char) == 1:
        print("Char is :", char)
        # break
