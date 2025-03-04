from math import sqrt

# math operations
a = 3
b = 8
print(a + b) # 
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(sqrt(a**10 + b**10))

# BMI calculation
a = 65
b = 1.75
floor = 18.5
celing = 25
c = a / b ** 2
if c < floor:
    print("Underweight")
elif c > celing:
    print("Overweight")
else:
    print("Normal weight")

# String price
a = "Knock, knock!! Who's there?! Python who? Python is a programming language!"
length = len(a)
price = 0.6
whole_part = int(price * length)
remainder = int(round((price * length - whole_part) * 100, 2))
print(f"{whole_part} dollars & {remainder} cents.")
space_count = a.count(" ")
words = a.split()
words_count = len(words)
print(f"space count {space_count}, words count {words_count}")

# Chinese zodiac
years_dict = { 
    8: "Dragon", 
    9: "Snake", 
    10: "Horse", 
    11: "Goat", 
    0: "Monkey", 
    1: "Rooster", 
    2: "Dog", 
    3: "Pig", 
    4: "Rat", 
    5: "Ox", 
    6: "Tiger", 
    7: "Rabbit"
}
year = 2020
index = year % 12
print(years_dict[index])

# Reverse number
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
    print(int(b))

# Standard American Convention
num = 1234567890
print(f"{num:,}")

# Josephus problem
n = 50
k = 25      
j = 0
for i in range(1, n + 1):
    j = (j + k) % i
print(j + 1)

# Dots count
dots_count = int(input().strip())

dots = []

for i in range (dots_count):
    x, y = map(int, input().split())
    dots.append((x, y))
print(dots)

q1 = q2 = q3= q4 = 0

for x, y in dots:
    if x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    elif x > 0 and y < 0:
        q4 += 1
print(f"Первая четверть: {q1}\nВторая четверть: {q2}\nТретья четверть: {q3}\nЧетвертая четверть: {q4}")

# Bigger then previous
n = str('1 2 3 4 5 6 7 8 9')
numbers = list(map(int, n.split()))
numbers_count = len(numbers)
bigger = 0
for i in range(1, numbers_count):
    if numbers[i] > numbers[i - 1]:
        bigger += 1
print(bigger)

# Back, forward and vice versa
n = '1 2 3 4 5 6 7 8 9'
numbers = list(map(int, n.split()))
numbers_count = len(numbers)
for i in range(0, numbers_count - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
print(*numbers)

# Developmental shift
n = '1 2 3 4 5 6 7 8 9'
numbers = list(map(int, n.split()))
last_number = numbers[-1]
new_numbers = [last_number] + numbers[:-1]
print(*new_numbers)

# Various elements
n = '1 2 3 4 5 6 7 8 9 9 9 9 9'
numbers = list(map(int, n.split()))
new_numbers = []
for number in numbers:
    if number not in new_numbers:
        new_numbers.append(number)
print(len(new_numbers))

# Product of numbers
numbers_count = int(input().strip())
numbers = list(map(int(input().split() for _ in range(numbers_count))))
product = int(input().strip())
flag = False
for i in range(numbers_count):
    for j in range(i+1, numbers_count):
        if numbers[i] * numbers[j] == product:
            flag = True
            break
print("YES" if flag else "NO")


