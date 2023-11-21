import os

print_red = lambda x: print("\033[31m{}\033[0m".format(x))
print_green = lambda x: print("\033[32m{}\033[0m".format(x))
print_yellow = lambda x: print("\033[33m{}\033[0m".format(x))

if os.listdir(".") != []:
    print_red("Directory is not empty")
    exit(1)


