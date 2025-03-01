from math import sqrt
'''
a = 3
b = 8
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(sqrt(a**10 + b**10))

a = 65
b = 1.75
floor = 18.5
celing = 25
c = a / b ** 2
if c < floor:
    print("Недостаточная масса")
elif c > celing:
    print("Избыточная масса")
else:
    print("Норма")

a = "Привет, как    дела?!"
length = len(a)
price = 0.6
whole_part = int(price * length)
remainder = int(round((price * length - whole_part) * 100, 2))
print(f"{whole_part} р. и {remainder} коп.")
space_count = a.count(" ")
words = a.split()
words_count = len(words)
print(f"количство пробелов {space_count}, количество слов {words_count}")

years_dict = { 8 : "Дракон", 
               9 : "Змея", 
               10 : "Лошадь", 
               11 : "Овца", 
               0 : "Обезьяна", 
               1 : "Петух", 
               2 : "Собака", 
               3 : "Свинья", 
               4 : "Крыса", 
               5 : "Бык", 
               6 : "Тигр", 
               7 : "Заяц"}
year = 2020
index = year % 12
print(years_dict[index])

a = str(355676)
b = a[0] + a[:-6:-1]
print(int(b))

a = str(35567)
b = a[::-1]
print(int(b))

if len(a) == 5:
    a = str(a)
    b = a[0] + a[:-6:-1]
    print(int(b))
else:
    a = str(a)
    b = a[::-1]
    print(int(b))'''


