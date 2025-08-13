"""
1 American mile = 1609.344 metres;
1 American gallon = 3.785411784 litres.
"""

def liters_100km_to_miles_gallon(liters):
    #
    # Write your code here.
    #
    american_mile = 1609.344 #meters
    american_gallon = 3.785411784 #litres

    gallon = liters / american_gallon
    miles = 100 * 1000 / american_mile

    return miles / gallon

def miles_gallon_to_liters_100km(miles):
    #
    # Write your code here.
    #
    american_mile = 1609.344 #meters
    american_gallon = 3.785411784 #litres

    kilometers = miles * american_mile / 1000 / 100
    liters = american_gallon

    return liters / kilometers


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print("-----------")
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
