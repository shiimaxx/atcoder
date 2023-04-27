import math
for i in range(int(input()), 0, -1):
    if math.sqrt(i).is_integer():
        print(i)
        break
