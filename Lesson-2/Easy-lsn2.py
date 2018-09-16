# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

my_list = ['яблоко', 'банан', 'киви', 'арбуз']
max_len = 0
for a in my_list:
   if max_len <= len(a):
       max_len = len(a)
for num, fruit in enumerate(my_list, start=1):
    print('{0}.{1:>{2}}'.format(num,fruit,max_len+1))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

my_list1 = ['Day', 3151, 10.05, 12, 'True', 'Wood']
my_list2 = ['Alex', 10.05, 'Katy', 17, 'Wood', 'False']
for f in my_list1:
    for d in my_list2:
        if f == d:
            my_list1.remove(f)
print(my_list1)



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

num_list = [137, 12, 76, 229, 1000, 657, 85, 64]
for f in num_list:
    if f % 2 == 0:
        f /= 4
    else:
        f *= 2
    print(f)