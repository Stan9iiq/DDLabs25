numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

a = -99
summ = 0
avr = 0
lenght = len(numbers)

for i in range(0, lenght):
    if numbers[i] != None:
        summ += numbers[i]
    else:
        a = i
avr = summ/(lenght)
numbers[a] = avr

print("Измененный список:", numbers)
