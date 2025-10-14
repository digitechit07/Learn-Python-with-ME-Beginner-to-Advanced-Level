#Conditional Statment
# Check if a number is divisible by both 3 and 5.○ Input: num = 15
num = int(input("enter a num: "))
if(num % 3 == 0 and num % 5 ==0):
     print("divisible by both 3 and 5")
else:
     print("Not divisible by both 3 and 5")

# 2. Determine if a string’s length is even and contains only lowercase letters.
s = (input("Enter a letters: "))
if len(s) % 2 == 0 and s.lower():
    print("Even length and all lowercase")
else:
     print(" Not Even length and all lowercase")

# 3. Check if the first and last characters of a string are the same (case-sensitive).
s = input("enter a string: ")
if s[0] == s[-1]:
    print("First and last character are same")
else:
    print("First and last character are different")

# 4. Verify if a list has exactly 5 elements and the sum of elements is even.
lst = [2, 4, 6, 8, 10]
if len(lst) == 5 and sum(lst) % 2 == 0:
      print("List has 5 element with even sum")
else:
     print("List has 5 elements with odd sum or incorrect sum")

# 5. Check if a number is positive, negative, or zero and divisible by 4
num = int(input(" enter a num: "))
if (num > 0 and num % 4 == 0):
    print("Positive anddivisible by 4")
elif (num < 0):
     print("Negative and Not divisible by 4")
# 7. Check if the second element of a list is a string and has more than 3 characters.

lst = [1, "hello", 3]
if isinstance(lst[1], str) and len(lst[1]) > 3:  # for type of string
   print("Second element is a string with more than 3 characters")
else:
  print("Second element is a string with 3 or fewer characters")

# 8. Verify if a number is between 10 and 50 (inclusive) and is odd.

num = int(input("enter a num: "))
if num >= 10 == 50 and num % 3 == 0:
   print("Number is betwwen 10 and 50 and odd")
else:
   print("Number is between 10 and 50 but is not odd")

# 9. Check if a list’s first element is greater than its last element and both are positive.
lst =[10, 5, 3]
if lst[0] >= lst[-1] > 0:
     print("First element greater than last and both positive")
else:
  print("First element is not greater than last or both not positive")

lst =[3, 5, 10]
if lst[0] >= lst[2]:
    print("First element greater than last and both positive")
else:
   print("First element is not greater than last or both not positive")

# String Function:
# 12. Count the number of vowels in a string (case-insensitive).

s = input("Enter a string") 
vowels = "aeiou"
count = sum(1 for char in s.lower() if char in vowels)
print(count)

# 13. Replace all spaces in a string with underscores.

s = "hello world"
print(s.replace("hello world", "hello_world"))
s = "no spaces"
print(s.replace("no spaces", "no_spaces"))

# 14. Check if a string contains only alphabetic characters.

s = input("enter your alphabetic letter: ")
if s.isalpha():    #check if all letters are alphabetic than return ture 
   print("Alphabetic only")
else:
    print("Non Alphabetic only")

# 15. Convert a string to title case and check if it starts with ‘A’.

s = input("enter a string")
title_s = s.title()
if title_s.startswith("A"):
    print("Title case start with A")
else:
    print("Title case does not start with A")

# 17. Check if a string is all uppercase and has no spaces

s = input("enter a string: ")
if s.isupper() and "" not in s:
   print("All uppercase and no space")
else:
   print("Contains spaces or not all uppercase")

# 18. Remove all vowels from a string (case-insensitive) and return the result.


s = input("enter a string")
vowels = "aeiouAEIOU"
result = " ".join(char for char in s if char not in vowels)
print(result)

# 19. Check if a string contains the substring "py" (case-sensitive).

s = input("enter a string")
if "py" in s:
    print("Contans py")
else:
    print("Does not contains py")

# 20. Swap the case of all characters in a string.

s = input("enter a string")
if s.swapcase():
     print("pYtHoN")
else:
   print("hELLO123")

# Indexing Q8uestions

# 21. Get the third character of a string if it exists, else return "Too short"
s = "python"
if(s[2]):
    print("t")
else:
    print("too short")

# 22. Check if the second element of a list is a number greater than 10.
lst = [1, 15 ,3]
if lst[0] < 10:
    print("Second element ia a number greater than 10")
else:
    print("second element is not greater than number 10")

# 23. Return the last character of a string if it’s alphabetic, else "Not alphabetic"
s = "hello"
last_char = s[-1]
if last_char.isalpha():
    print(last_char)
else:
    print("Not alphabetic")

# 24. Get the first element of a list if it’s a string, else return "Not a string".
lst = ["apple", 2, 3]
first_char = lst[0]
if isinstance(first_char, str):
    print("apple")
else:
    print("Not a string")

# 27. Check if the first character of a string is uppercase
s = input("enter a string: ")
first_char = s[0]
if first_char. isupper():
    print("First character is uppercase")
else:
   print("First character is not uppercase")

# 28. Get the middle character of a string (if length is odd) or "Even length".
s = "abcde"
length = len(s)
if length % 2 != 0:
    middle_character = s[length // 2]
    print("c")
else:
    print("Even length")

# 29. Check if the last element of a list is divisible by 3.
lst = [1, 2, 6]
last_char = lst[-1]
if last_char % 3 == 0:
    print("Last element is divisible by 3")
else:
    print("Last element not divisible by 3")

# 30. Return the first character of a string if it’s not a digit, else "Digit".
s = input("enter a string")
if s[0].isdigit():
   print("digit ")
else:
    print("h")

#Slicing Questions:    
# 36. Return a list without its first 2 elements if possible, else return empty list.
lst = [1, 2, 3, 4]
if len(lst) >=2:
    print(lst[-2])   # second to last element
else:
    print("list iss too short")

# 35. Get the first half of a string (round down for odd length).
s = "python"
if s[0:2]:
    print("pyt")
else:
    print("hi")

# 39. Return a list containing only its even-indexed elements.
lst = [1, 2, 3, 4, 5]
if lst[1:4]:
    print(2, 3, 4, 5)
else:
    print(1, 2, 3)

# 33. Return a string without its first and last characters if length is at least 2.
s = "hello"
if len(s) >= 3:
    print(s[1:4])
else:
    print("Too short")


lst = [1, 2, 3, 4, 5]
if lst[1] and lst[3]:
    print(lst[1], lst[3])
else:
    print()
# 31. Extract the first 3 characters of a string if possible, else return the entire string
s = "python"
half = len(s) // 2
print(s[:half])

# 36. Return a list without its first 2 elements if possible, else return empty list.
lst = [1, 2, 3, 4]
if len(lst):
    print(lst[2:])
else:
    print([])

# 37. Extract characters from index 2 to 5 (inclusive) of a string if possible.

s = "python"
if len(s):
    print(s[2:5])
else:
    print("")

# 38. Get the last 3 characters of a string in reverse order.
s = "python"
if len(s) // 2:
    print(s[-5:-3])
else:
    print("")


# List Questions
#41. Check if a list contains at least one string and one number.
lst = [1, "hello", 3]

lst_str = any(isinstance(x, str) for x in lst)
lst_num = any(isinstance(x, (int, float)) for x in lst)

if lst_str and lst_num:
    print("Contains both string and number")
else:
    print("Does not contain both string and number")

#42. Return a list with all elements doubled if they are numbers.
lst = [1, 2, "hello", 3]
result = [x * 2 if isinstance(x, (int, float)) else x for x in lst]
print(result)

#43. Check if a list has duplicate elements.
lst = [1, 2, 2, 3]
if len(lst) != len(set(lst)):
    print("Has duplicates")
else:
    print("No duplicates")

#44. Create a list containing only the string elements of the input list.
lst = [1, "apple", 2, "banana"]
result = [x for x in lst if isinstance(x, str)]
print(result)

#45. Check if all elements in a list are positive numbers.
lst = [1, -2, 3]
if all(isinstance(x, (int, float)) and x > 0 for x in lst):
    print("All positive numbers")
else:
    print("Not all poistive numbers")

#45. Check if all elements in a list are positive numbers.
lst = [1, 2, 3]
if len(lst) >= 2:
    lst[0], lst[-1] = lst[-1], lst[0]
print(lst)

#49. Check if a list contains exactly 3 strings.

lst = ["apple", "banana", "cherry"]  

count_str = sum(isinstance(x, str) for x in lst)

if count_str == 3:
    print("Exactly 3 strings")
else:
    print("Not exactly 3 strings")