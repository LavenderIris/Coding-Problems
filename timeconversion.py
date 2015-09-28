num = 6

for i in range(0, num):
    numspaces = num - i
    for j in range(0, num):
        if j < (numspaces - 1):
            print('.', end="")
        else:
            print('#', end="")
    print()
