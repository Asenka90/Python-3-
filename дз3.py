#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print ('Задача 1')
from random import randint
list = []
i = 1
n = int(input('Введите количество элементов в списке: '))
for i in range(n):
    list.append(randint(1,9))
    i += 1
print(f'Ваш список из {n} элементов: {list}')
j=1
sum=0
while j < len(list):
    sum=sum+list[j]
    j+=2
print(f'Сумма элементов списка, стоящих на нечётной позиции: {sum}')

#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

print ('Задача 2')
from random import randint
list1 = []
i = 1
n = int(input('Введите количество элементов в списке: '))
for i in range(n):
    list1.append(randint(1,9))
    i += 1
print(f'Ваш список из {n} элементов: {list1}')
count=0
j=1
if n%2==0:
    while count<len(list1)//2:
        m=list1[count]*list1[len(list1)-j]
        print(m)
        count+=1
        j+=1
    else:
        while count<len(list1)//2:
            m=list1[count]*list1[len(list1)-j]
            print('Произведения пар чисел списка:')
            print(m)
            print(list1[len(list1)//2]**2)
            count+=1
            j+=1

#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print ('Задача 3')
list2 = [18.6, 19.8, 6.5, 63.1, 4.9]
print(f'Ваш список: {list2}')
def dif(list2):
    dif_max_min = []
    for i in range(len(list2)):
        dif_max_min.append(list2[i] % 1)
    return max(dif_max_min) - min(dif_max_min)
print('Разница между максимальным и минимальным значением дробной части элементов: ', round(dif(list2), 2))

#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

print ('Задача 4')
x = int(input('Введите число: '))
bin = ''
while x > 0:
    bin = str(x % 2) + bin
    x = x // 2
print('В двоичной системе это: ',bin)

#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

print ('Задача 5')
n2 = int(input('Введите число n: '))
fib = [0] * (n2 * 2 + 1)
fib[n2] = 0
fib[n2 + 1] = 1
for i in range(n2 + 2, len(fib)):
    fib[i] = fib[i - 2] + fib[i - 1]
for i in range(n2, -1, -1):
    fib[i] = fib[i + 2] - fib[i + 1]
print(fib)
