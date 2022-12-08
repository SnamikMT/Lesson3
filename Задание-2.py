#2 задание
startX, startY = 0, 0
while True:
    a = input("Введите координату перемещения u-вверх, d-вниз, l-влево, r-вправо, stop - конец: ")
    if a == "u":
        startY += 1
    elif a == "d":
        startY -= 1
    elif a == "r":
        startX += 1
    elif a == "l":
        startX -= 1
    elif a == "stop":
        break
    print(f'Координаты: {startX, startY}')
