

name = input("What is the name of the beer? ")

water = int(input("How much did you pay for water? "))

receipt = int(input("How much did you pay for the ingredients? "))

cleaning = int(input("How much did you pay for cleaning products? "))

fuel = int(input("How much did you pay for fuel? "))

bottles = int(input("How much did you pay for bottles? ") )

labels = int(input("How much did you pay for packging and labels? "))

production = int(input("How many marketable bottles did this Mash produce? "))

count = (water+receipt+cleaning+fuel+bottles+labels)

print("This receipt costed R$"+str(count)+".")

each = (count/production)

print("Each bottle costed R$"+str(each)+".")

price_count = (count+250)

price = (price_count/production)

print("Each bottle of the "+name+" should be sold at a minimum of R$"+str(price)+".")


