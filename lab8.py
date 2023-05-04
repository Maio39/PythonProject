#Let's learn about list

supplies = ["test", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 89.3, True]

#Add object to list
#METHOD 1
#supplies.append("toilet paper")
#supplies.append("bidet")

#METHOD 2
#supplies.extend(["toilet paper", "bidet"])

#METHOD 3
#supplies = supplies + ["toilet paper", "bidet"]

#Add object to start of list
supplies.insert(0,"bidet")

#Add toilet paper to the penultimate position on the list
supplies.insert(-1,"toilet paper")

print(supplies)