#Let's learn about list

supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 89.3, True]

supplies.extend(["toilet paper", "bidet"])

#Delete all data into the list
#supplies.clear()

#Delete specific element in the list
#supplies.remove("tent")
#supplies.remove("sleeping bags")

#Delete specific element in the list by index
print(supplies.pop(0))
supplies.pop(0)


print(supplies)