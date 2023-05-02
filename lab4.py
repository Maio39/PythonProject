#if, else, comparison operators

print("Hello, welcome to Maio39 Coffee!!")

name = input("What is your name?\n")

if name == "Ben":
    evil_status = input("Are you Evil?\n")
    if evil_status == "Yes":
        print("You're not welcome here Evil Ben!! Get Out!!")
        exit()
    else:
        print("Hello " + name + ", thank you so much for coming today!!\n\n")
else:
    print("Hello " + name + ", thank you so much for coming today!!\n\n")

#if 2 > 3:
    #print("Yep, It's True")
    #print("It's Still True")
#else:
    #print("Nope, not true!!")