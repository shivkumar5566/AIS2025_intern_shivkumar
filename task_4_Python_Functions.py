 # Task 4: Python Functions

## A. User-defined Functions:

# 1. Function to return list of squares
def square_list(numbers):
    return [x**2 for x in numbers]

print("Squares:", square_list([1, 2, 3, 4]))  

# 2. Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print("Vowel Count:", count_vowels("Hello World")) 

# 3. Function to check Armstrong number
def is_armstrong(num):
    power = len(str(num))
    return num == sum(int(digit) ** power for digit in str(num))

print("Is Armstrong (153):", is_armstrong(153)) 

# 4. Function to return names starting with 'S'
def names_starting_with_s(names):
    return [name for name in names if name.startswith('S')]

print("Names starting with 'S':", names_starting_with_s(["Sopna", "Altamash", "Shivkumar", "Abhishak"]))  

# 5. Function to return HCF of two numbers
def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

print("HCF of 60 and 48:", compute_hcf(60, 48)) 


## B. Lambda Functions:

# 1. Check if number divisible by 5
divisible_by_5 = lambda x: x % 5 == 0
print("Divisible by 5 (25):", divisible_by_5(25)) 

# 2. Convert Celsius to Fahrenheit
c_to_f = lambda c: (c * 9/5) + 32
print("C to F (0):", c_to_f(0)) 

# 3. Return cube of a number
cube = lambda x: x ** 3
print("Cube of 3:", cube(3)) 

# 4. Add two strings
add_strings = lambda a, b: a + b
print("Add strings:", add_strings("Hello", "World"))  

# 5. Check if string length > 8
long_string = lambda s: len(s) > 8
print("Length > 8 (\"OpenAI GPT\"):", long_string("OpenAI GPT")) 


## C. Filter Function:

# 1. Strings with length > 4
strings = ["cat", "tiger", "lioness", "dog"]
long_strings = list(filter(lambda x: len(x) > 4, strings))
print("Strings > 4 chars:", long_strings)  

# 2. Numbers > 100
numbers = [45, 200, 78, 150, 230]
large_numbers = list(filter(lambda x: x > 100, numbers))
print("Numbers > 100:", large_numbers) 

# 3. Filter odd numbers
num_list = [1, 2, 3, 4, 5, 6, 7]
odds = list(filter(lambda x: x % 2 != 0, num_list))
print("Odd numbers:", odds) 
# 4. Names ending with 'a'
names = ["Nita", "Sita", "Soham", "Anita"]
ends_with_a = list(filter(lambda x: x.endswith('a'), names))
print("Names ending with 'a':", ends_with_a)  

# 5. Filter non-integer values
mixed = [1, "hello", 3.5, 4, True, 5]
integers_only = list(filter(lambda x: type(x) == int, mixed))
print("Integers only:", integers_only) 


## D. Format Function:

# 1. Format string example
name = "Sopan"
marks = 89
subject = "Math"
print("Student {name} scored {marks} marks in {subject}".format(name=name, marks=marks, subject=subject))



## E. Map Function:


# 1. Squares using map
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print("Squares using map:", squares)  

# 2. Convert list of strings to uppercase
words = ["hello", "world"]
uppercase_words = list(map(str.upper, words))
print("Uppercase:", uppercase_words) 

# 3. Subtract 2 from each number
numbers = [5, 10, 15, 20]
subtract_two = list(map(lambda x: x - 2, numbers))
print("Subtract 2:", subtract_two)  

# 4. Length of each word in a sentence
sentence = "Python is fun and powerful"
word_lengths = list(map(len, sentence.split()))
print("Word lengths:", word_lengths) 

# 5. Multiply each element by its index
values = [10, 20, 30, 40]
multiplied = list(map(lambda x: x[0] * x[1], enumerate(values)))
print("Element * index:", multiplied) 


