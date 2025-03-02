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
