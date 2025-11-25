size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_chesse = input("Do you want extra cheese? Y or N: ")
price = 0

# S = 15
# M = 20
# L = 25
# Pepperoni for small = +2
# Pepperoni for medium or large = +3
# Extra Cheese = +1

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25

else:
    print("Wrong input")

if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_chesse == "Y":
    price += 1

print(f"Total price is ${price}.")
