lst = [4, 2, 3, 2, 1, 4]
def my_count(l: list, item):
    c = 0
    for el in l:
        if el == item:
            c += 1
    return c
print(my_count(lst, 4))