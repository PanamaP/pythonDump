
n_tuple = ("mús", [8, 4, 6], (1, 2, 3))
print(n_tuple[0][1], n_tuple[0][2])

for holf in n_tuple:
    for stak in holf:
        print(stak, end=' ')
    print()

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[:-4])