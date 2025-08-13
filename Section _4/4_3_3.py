def strange_list_fun(n):
    strange_list = []
    strange_list2 = []

    for i in range(0, n):
        strange_list.insert(0, i)
        strange_list2.append(i)

    return strange_list, strange_list2


print(strange_list_fun(5))