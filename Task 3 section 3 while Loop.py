i = 1
while i <= 10:
    print(i)
    i += 1

total = 0
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter a number (0 to stop): "))
print("Total sum:", total)

num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed:", rev)

num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Digit count:", count)

n = int(input("Enter number of terms: "))
a, b = 0, 1
count = 0
while count < n:
    print(a)
    a, b = b, a + b
    count += 1

num = int(input("Enter a number: "))
s = 0
while num > 0:
    s += num % 10
    num //= 10
print("Sum of digits:", s)

num = 1
while num <= 1000:
    print(num)
    num *= 2

secret = 7
guess = -1
while guess != secret:
    guess = int(input("Guess the number: "))
print("Correct guess!")

n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i)
    i += 2

string = input("Enter a string: ")
i = len(string) - 1
while i >= 0:
    print(string[i], end="")
    i -= 1

