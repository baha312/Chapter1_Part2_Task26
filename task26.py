#  Напишите функцию которая подсчитает количество четных и нечетных чисел в списке чисел.

all_ = input("Введите числа: ").split(",")

result_even = []
result_odd = []

for i in all_:
    if int(i) % 2 ==0:
        result_even.append(i)
    elif int(i)% 2 != 0:
        result_odd.append(i)

print('Количество четных чисел: ',len(result_even))
print('Количество нечетных чисел: ',len(result_odd))