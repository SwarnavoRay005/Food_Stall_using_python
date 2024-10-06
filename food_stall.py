menu = {
    "popcorn": 250.0,
    "burger": 175.0,
    "coke": 120.25,
    "fries": 75.25,
    "pizza": 100.0,
    "smoothie": 90.0
}

cart = []
total = 0

print("------MENU------")
for key, value in menu.items():
    print(f"{key:10}: Rs. {value:.2f}")

print("----------------")

while True:
    food = input("enter the food items ( Press Q to quit ):").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("the chosen items are:")
for i in cart:
    print(i)

for food in cart:
    total = total+menu.get(food)

print(f"the total bill is: {total}")

