#Let's start a coffee shop together!! We're going to build
# a coffee shop using some new Python Programming concepts.

#Let's build robot Barista!!

print("Hello, welcome to Maio39 Coffee!!")

name = input("What is your name?\n")

print("Hello " + name + ", thank you so much for coming today!!\n\n")

price = 8

menu = "Black coffee, Espresso, Latte, Cappuccino"

#Metodo 1
#print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)
#order = input()

#Metodo 2
order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\nPrice: $" + str(price) +"\n")

quantity = input("How many do you want?\n")

total = price * int(quantity)

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.\nThe final price is $" + str(total))