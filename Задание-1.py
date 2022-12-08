#1 задание
coordinate = input("Введите координаты перемещения u-вверх, d-вниз, l-влево, r-вправо: ")
startX, startY = 0, 0
for i in coordinate:
    if i == "u":
        startY += 1
    elif i == "d":
        startY -= 1
    elif i == "r":
        startX += 1
    elif i == "l":
        startX -= 1
print(f'Координаты: {startX, startY}')


