def safe_print_list(my_list=[], x=0):
    y = 0
    for i in range(x):
        try:
            print(my_list[y],end="")
            y += 1
        except:
            break
    return y
