# Suggest transport according distance

dist = int(input("Enter distance : "))

if dist < 3:
    use = "walk"
elif dist <= 10:
    use = "bike"
elif dist >=10:
    use = "car"

print(use)
