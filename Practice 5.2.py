# Розмірність масиву
rows = 7
cols = 7

# Ініціалізація порожнього двовимірного масиву
matrix = [[0 for j in range(cols)] for i in range(rows)]

# Заповнення масиву елементами з клавіатури
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input(f"Введіть елемент [{i+1}][{j+1}]: "))

# Виведення заповненого масиву
print("Двовимірний масив:")
for row in matrix:
    print(row)