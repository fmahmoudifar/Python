print ("Wlcome to the rollercoaster!")
height = int(input("Please enter your height in cm: "))

if height >= 120:
    print ("you can pleay the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print ("Sorr, you have to grow taller before you can ride. ")