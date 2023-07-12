#making the lists
pizzas_List = ['Margarita', 'Cheese', 'Farm Fenzy', 'Veg Mushroom Pizza']
toppings_List = ['Mushroom', 'Peri Peri Sause', 'Green pepper', 'Extra cheese']
prices_pizza = {'Margarita': 150,  'Cheese': 160, 'Farm Fenzy': 180, 'Veg Mushroom Pizza': 165}
topping_prices = {'Mushroom':15, 'Peri Peri Sause': 20, 'Green pepper':25, 'Extra cheese':40}
total = []
final_order = {}
adress = {}

print("Order the Pizza")
PIZZA = True
while PIZZA:    
    print("Choose your pizza from below List :-  ")
    print()
    for pizzas in pizzas_List:
        print(pizzas)
        print()
    while True:
        pizza = input("Choose your pizza :- ")
        if pizza in pizzas_List:
            print(f"You have choosed a {pizza}.")
            total.append(prices_pizza[pizza])
            break
        if pizza not in pizzas_List:
            print(f"The choosed pizza is not available {pizza}.")

    
    toppingOrder = True
    print("Choose your toppings :-  ")
    for toppings in toppings_List:
        print(toppings)
        print()

    while toppingOrder:
        extra_topping = input("Do you want extra topping? (yes/no)")
        if extra_topping == "yes":
            topping = input("choose the toppings :-")
            if topping in toppings_List:
                final_order.setdefault(pizza, []) 
                final_order[pizza].append(topping)
                print(f"topping is added {topping}.")
                total.append(topping_prices[topping])
            else:
                print(f"Choosed topping is not available")

        elif extra_topping == "no":
            break
    extra_pizza = input("Do you want to add more pizza ?")
    if extra_pizza == "no":
        for key, value in final_order.items():
            print(f"\nPizza :-  {key} Extra toppings :-  {value}")
    PIZZA = False


print(f"\nTotal Bill :- {sum(total)}")
print("Address :- ")
adress['Name'] = input("Enter name:- ")
adress['street'] = input("Enter your adress :- ")
adress['Mobile'] = input("What is your Mobile Number?")
print("Your Pizza will be delivered soon!")
print(adress['street'])
print(adress['Mobile'])
