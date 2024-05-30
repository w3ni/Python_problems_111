# Coffee order program

order_size = input("Enter order size [S/M/L] :::: ")
extra_shot = input("Do you want extra shot y/n : ")

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " Coffee"


print("ORder :", coffee)
