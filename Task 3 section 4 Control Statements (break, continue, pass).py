for i in range(1, 11):
    if i == 5:
        break
    print(i)

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

for i in range(5):
    if i == 2:
        pass  # placeholder for future logic
    print(i)

nums = [4, 7, 2, 9, 5]
target = int(input("Enter number to search: "))
for num in nums:
    if num == target:
        print("Found:", num)
        break

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)

text = input("Enter text: ")
for ch in text:
    if ch.lower() in 'aeiou':
        print("First vowel found:", ch)
        break

x = 10
if x > 5:
    pass  # logic to be added later
print("Done")

total = 0
for i in range(1, 100):
    total += i
    if total > 50:
        print("Breaking at total:", total)
        break

text = input("Enter text: ")
for ch in text:
    if ch.isupper():
        continue
    print(ch, end="")


