blocks = int(input("Enter the number of blocks: "))
#
# Write your code here.
#
height = 0
base = 1

while blocks >= base:
    height += 1
    blocks -= base
    base += 1

print("The height of the pyramid:", height)