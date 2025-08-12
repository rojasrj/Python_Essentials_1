c0 = int(input("Enter a number: "))
counter = 0

if c0 > 0:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = int(c0 / 2)
            print(c0)
        elif c0 % 2 != 0:
            c0 = int(3 * c0 + 1)
            print(c0)
        counter += 1
    print("Steps = ", counter)
else:
    print("Not a non-zero or positive number")