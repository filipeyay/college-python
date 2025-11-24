height = int(input("What is your height in cm? "))
bill = 0


if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("\nWhat is your age? "))

    if age <= 18:
        bill = 7
        print("Your ticket will cost $12.")
    elif age < 12:
        bill = 5
        print("Your ticket will cost $5.")
    elif age >= 45 and age <= 55:
        print("You have a free ticket!")
    else:
        bill = 12
        print("Your ticket will cost $7.")

    photo = input("Do you want a photo take? Type y for Yes and n for No. ")
    if photo == "y":
        bill += 3

    print(f"Your final bill is {bill}.")

else:
    print("You cannot ride ride the rollercoaster.")
