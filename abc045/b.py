SA = list(input())
SB = list(input())
SC = list(input())

drawer = SA
while True:
    if len(drawer) == 0:
        break
    draw = drawer.pop(0)
    if draw == 'a':
        drawer = SA
    elif draw == 'b':
        drawer = SB
    elif draw == 'c':
        drawer = SC

print('A') if drawer is SA else print('B') if drawer is SB else print('C')
