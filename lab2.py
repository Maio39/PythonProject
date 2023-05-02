#Let's start a coffee shop together!! We're going to build
# a coffee shop using some new Python Programming concepts.

#Let's build robot Barista!!

print("Hello, welcome to Maio39 Coffee!!")

name = input("What is your name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you Evil?\n")
    good_deeds = int(input("How many Good deeds have you done today?\n"))
    if evil_status == "Yes" and good_deeds < 4:
        print("You're not welcome here Evil " + name + "!! Get Out!!")
        exit()      
    else:
        print("Hello " + name + ", you did good deeds today. Thank you so much for coming today!!\n\n") 
else:
    print("Hello " + name + ", thank you so much for coming today!!\n\n")

menu = "Black coffee, Espresso, Latte, Cappuccino, Frapuccino"

#Metodo 1
#print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)
#order = input()

#Metodo 2
order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

quantity = input("How many do you want?\n")

price = 0

if order == "Frapuccino":
    price = 5
elif order == "Black coffee":
    price = 2
elif order == "Espresso":
    price = 1
elif order == "Latte" or order == "Capuccino":
    price = 3

if price == 0:
    print("The product you selected does not exist.")
else:
    total = price * int(quantity)
    print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.\nThe final price is $" + str(total))