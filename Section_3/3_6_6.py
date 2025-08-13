my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 6, 1, 2, 0]
# Write your code here.
tmp_element = my_list[:]

for element in tmp_element:
    if my_list.count(element) >= 2:
        my_list.remove(element)
        my_list.sort()

print("The list with unique elements only:")
print(my_list)