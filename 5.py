my_list = [7, 5, 3, 3, 2]
print(f"Rating - {my_list}")
digit = int(input("Insert a number (111 - exit) "))
while digit != 111:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"Current list - {my_list}")
    digit = int(input("Insert a number "))