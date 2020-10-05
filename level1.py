for x in range(1000000):
    if x % 5 == 2:
        if x % 7 == 6:
            if x % 13 == 9:
                print("Solution found {}".format(x))
    if x % 1000 == 0:
        print(x)