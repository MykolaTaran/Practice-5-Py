# Введення розміру масиву
N = int(input("Введіть розмір масиву: "))

# Ініціалізація масиву
array = []
for i in range(N):
    num = int(input(f"Введіть {i+1}-й елемент масиву: "))
    array.append(num)

# Обчислення добутку ненульових непарних елементів
product = 1
for num in array:
    if num != 0 and num % 2 != 0:
        product *= num

# Виведення результату
print(f"Добуток ненульових непарних елементів масиву: {product}")