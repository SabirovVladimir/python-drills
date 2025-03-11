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
print(f"First quarter: {q1}\nSecond quarter: {q2}\nThird quarter: {q3}\nFourth quarter: {q4}")

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

# rock paper scissors
Rus = str(input())
Tim = str(input())
if Rus == 'Rock' and Tim == 'Scissors':
    print('Rus WIN')
elif Rus == 'Scissors' and Tim == 'Paper':
    print('Rus WIN')
elif Rus == 'Paper' and Tim == 'Rock':
    print('Rus WIN')
elif Rus == Tim:
    print('DRAW')
else:
    print('Tim WIN')

# rock paper scissors lizard spock
Rus = str(input())
Tim = str(input())
if Rus == 'Rock' and (Tim == 'Scissors' or Tim == 'Lizard'):
    print('Rus WIN')
elif Rus == 'Scissors' and (Tim == 'Paper' or Tim == 'Lizard'):
    print('Rus WIN')
elif Rus == 'Paper' and (Tim == 'Rock' or Tim == 'Spock'):
    print('Rus WIN')
elif Rus == 'Lizard' and (Tim == 'Spock' or Tim == 'Paper'):
    print('Rus WIN')
elif Rus == 'Spock' and (Tim == 'Rock' or Tim == 'Scissors'):
    print('Rus WIN')
elif Rus == Tim:
    print('DRAW')
else:
    print('Tim WIN')

# Heads and tails
string = 'ОРРОРОРООРРРО'
len_str = len(string)
max_count = 0
for i in range(len_str):
    count = 0
    if string[i] == 'Р':
        count += 1
    for j in range(i + 1, len_str):
        if string[j] == 'Р':
            count += 1
        else:
            break
    if count > max_count:
        max_count = count
print(max_count)

# Silicon Valley
n = int(input())
strings = list(str(input().strip()) for _ in range(n))
frig_num = []
for o in range (n):
    string = strings[o]
    word = []

    for char in string:
        if char == 'a' and len(word) == 0:
            word.append(char)
        elif char == 'n' and len(word) == 1:
            word.append(char)
        elif char == 't' and len(word) == 2:
            word.append(char)
        elif char == 'o' and len(word) == 3:
            word.append(char)
        elif char == 'n' and len(word) == 4:
            word.append(char)
    if len(word) == 5:
        frig_num.append(o+1)
print(*frig_num)

# Roskomnadzor banned the letter a
word = str(input().strip())
phrase = word + ' banned the letter'

letters = sorted(set(phrase.replace(' ', '')))
for letter in letters:
    print(phrase, letter)
    phrase = " ".join(phrase.split())
    phrase = phrase.replace(letter, '')

# Divisibility predicate
def func(num1, num2):
    return num1 % num2 == 0
num1, num2 = int(input()), int(input())
if func(num1, num2):
    print('YES')
else:
    print('NO')

# Nested lists
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].extend(sub_list)
print(list1)

list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = 0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if list1[i][j] > maximum:
            maximum = list1[i][j]
print(maximum)

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
new_list = []
for sublist in list1:
    sublist.reverse()
    new_list.append(sublist)
list1 = new_list
print(list1)

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        total += list1[i][j]
        counter += 1
average = total / counter
print(average)

# Sample list 1
n = 3
my_list = [[j + 1 for j in range(n)] for i in range(n)]
for row in my_list:
    print(*row)

# Sample list 2
n=3
my_list = [[j + 1 for j in range(i+1)] for i in range(n)]
for row in my_list:
    print(row)

# Pascal's Triangle 1
n = 3
def pascal(n):
    row = [1]
    for k in range(1, n + 1):
        row.append(row[-1] * (n - k + 1) // k)
    return row

print(pascal(n))

