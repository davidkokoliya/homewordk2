el_count = int(input("Insert a number of elements in the list "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Insert the next value in the list "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)