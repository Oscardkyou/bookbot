def find_numbers(n):
    numbers = []
    for i in range(1, n+1):
        numbers.append(i)
    return numbers

# Пример использования функции
n = int(input("Введите число: "))
result = find_numbers(n)
print(result)


