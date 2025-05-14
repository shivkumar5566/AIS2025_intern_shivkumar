for i in range(1, 11):
    print(i)

for i in range(2, 51, 2):
    print(i)
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)

text = input("Enter a string: ")
count = 0
for char in text.lower():
    if char in 'aeiou':
        count += 1
print("Vowel count:", count)

for i in range(1, 11):
    print(i**2)

total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)

string = input("Enter a string: ")
for char in string:
    print(char)

for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

