def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")

happy_new_year()

print("--------------")

happy_new_year(False)

print("--------------")

def boring_function():
    return 123


x = boring_function()

print("The boring_function has returned its result. It's:", x)

print("--------------")

def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2)) #True
print(strange_function(1)) #None