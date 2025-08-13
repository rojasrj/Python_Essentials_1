# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2, 90, 1, -9, 67]
new_list = my_list[:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

my_list = [10, 8, 6, 4, 2]
del my_list
#print(my_list)

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)