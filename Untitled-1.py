Problem 1: Separate Letters and Numbers
user_input = input("Enter a string with letters and numbers: ")
letters = []
numbers = []
for char in user_input:
  if char.isalpha():
    letters.append(char)
  elif char.isdigit():
    numbers.append(int(char))
word = "".join(letters)
total_sum = sum(numbers)
print(f'Word: "{word}", Sum: {total_sum}')[cite: 1]
Problem 2: Password Validator
import string
Check password based on length, uppercase, and special characters[cite: 1]
password = input("Enter your password: ")
has_upper = any(c.isupper() for c in password)
has_special = any(c in string.punctuation for c in password)
is_correct_length = 8 <= len(password) <= 16
if is_correct_length and has_upper and has_special:
  print("Password is Secure.")[cite: 1]
else:
  print("Password is NOT secure. Requirements: 8-16 chars, at least one uppercase and one special character.")
Problem 3: Store Discounts and Membership
Calculate discount based on price and membership status[cite: 1]
price = float(input("Enter total price: "))
is_member = input("Are you a Member? (Yes/No): ").strip().lower()
if price < 50:
  discount = 0.0
elif price <= 100:
  discount = 0.10
else:
  discount = 0.20
subtotal = price * (1 - discount)
final_total = subtotal * 0.95 if is_member == "yes" else subtotal
print(f"Final Total: ${final_total}")[cite: 1]
Problem 4: Common Names Finder

list1 = [name.strip() for name in input("Enter List 1 (comma-separated): ").split(",")]
list2 = [name.strip() for name in input("Enter List 2 (comma-separated): ").split(",")]

common_names = list(set(list1) & set(list2))
print(f"Common names: {common_names}")[cite: 1]
Problem 5: Student Averages & Honor Roll

students = {'Sam': [95, 90, 92], 'Alice': [85, 88, 90], 'Bob': [92, 94, 95]}

for name, scores in students.items():
  avg = sum(scores) / len(scores)
  if avg > 90:
    print(f"{name}: Average {avg:.1f} - Honor Roll")[cite: 1]
  else:
    print(f"{name}: Average {avg:.1f}")
Problem 6: Interleave Two Words

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

interleaved = "".join(c1 + c2 for c1, c2 in zip(word1, word2))
print(interleaved)[cite: 1]

num_str = input("Enter a multi-digit number: ")

while len(num_str) > 1:
  digit_sum = sum(int(digit) for digit in num_str)
  num_str = str(digit_sum)

print(f"Digital Root: {num_str}")[cite: 1]
Problem 8: Element Frequencies
from collections import Counter

numbers = [1, 1, 2, 3, 3, 3, 4]
freq_dict = Counter(numbers)
result = list(freq_dict.items())

print(result)[cite: 2]
Problem 9: Factorial and Divisibility

n = int(input("Enter a number n: "))

factorial = 1
for i in range(1, n + 1):
  factorial *= i

num_sum = sum(range(1, n + 1))

if factorial % num_sum == 0:
  print(f"Factorial is {factorial}, Sum is {num_sum}. {factorial} is divisible by {num_sum}.")[cite: 2]
else:
  print(f"Factorial is {factorial}, Sum is {num_sum}. {factorial} is not divisible by {num_sum}.")[cite: 2]
Problem 10: Shopping Cart System

store_prices = {'apple': 0.5, 'bread': 2.0, 'milk': 1.5}
cart = []

while True:
  action = input("Type 'Add [item]', 'Remove [item]', or 'Done' to finish: ")
  if action.lower() == 'done':
    break
  
  parts = action.split(maxsplit=1)
  if len(parts) < 2:
    print("Invalid format. Use 'Add item' or 'Remove item'.")
    continue
    
  command, item = parts[0].lower(), parts[1].lower()
  
  if command == 'add':
    if item in store_prices:
      cart.append(item)
    else:
      print(f"Error: '{item}' is not in the store.")[cite: 2]
  elif command == 'remove':
    if item in cart:
      cart.remove(item)
    else:
      print("Item not found in cart.")

total_bill = sum(store_prices[item] for item in cart)
print(f"Total Bill: ${total_bill}")[cite: 2]
Problem 11: Sentence Palindrome
# Check if a sentence is a palindrome, ignoring spaces and case[cite: 2]
sentence = input("Enter a sentence: ")
cleaned = "".join(char.lower() for char in sentence if char.isalnum())

is_palindrome = cleaned == cleaned[::-1]
print(is_palindrome)[cite: 2]
Problem 12: Number Square

# Create a square of numbers based on input n[cite: 2]
n = int(input("Enter n: "))

for i in range(1, n + 1):
  print(str(i) * n)[cite: 2]
Problem 13: Find Peaks in a List
# Find numbers greater than their left and right neighbors[cite: 2]
nums = [1, 5, 2, 6, 3]
peaks = []

for i in range(1, len(nums) - 1):
  if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
    peaks.append(nums[i])

print(f"Peaks: {peaks}")[cite: 2]

