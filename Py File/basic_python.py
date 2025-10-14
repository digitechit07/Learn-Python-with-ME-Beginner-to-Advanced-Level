def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is: {answer}")

def main():
    questions_and_answers = [
        ("What is the keyword to define a function in Python?", "def"),
        ("What data type is the result of: 3 + 2.5?", "float"),
        ("What is the output of: print(2 ** 3)?", "8"),
        ("How do you create a list in Python?", "Using square brackets"),
        ("What is the keyword to create a class in Python?", "class"),
        ("What is the method to add an element to a list?", "append"),
        ("How do you start a comment in Python?", "#"),
        ("What is the output of: print('Hello' + 'World')?", "HelloWorld"),
        ("How do you create a dictionary in Python?", "Using curly braces"),
        ("What is the keyword to import a module in Python?", "import"),
        # Add more questions here
    ]

    for question, answer in questions_and_answers:
        ask_question(question, answer)

if __name__ == "__main__":
    main()
    ("What is the output of: print(10 // 3)?", "3"),
    ("What is the method to remove an element from a list?", "remove"),
    ("How do you create a tuple in Python?", "Using parentheses"),
    ("What is the keyword to handle exceptions in Python?", "try"),
    ("What is the output of: print(len('Python'))?", "6"),
    ("How do you create a set in Python?", "Using curly braces"),
    ("What is the method to get the length of a list?", "len"),
    ("What is the output of: print(5 % 2)?", "1"),
    ("How do you create a string in Python?", "Using quotes"),
    ("What is the keyword to define a lambda function in Python?", "lambda"),
    ("What is the output of: print(2 * 3)?", "6"),
    ("How do you create a comment in Python?", "#"),
    ("What is the method to convert a string to lowercase?", "lower"),
    ("What is the output of: print(10 / 2)?", "5.0"),
    ("How do you create a boolean in Python?", "Using True or False"),
    ("What is the method to convert a string to uppercase?", "upper"),
    ("What is the output of: print(3 - 2)?", "1"),
    ("How do you create a dictionary in Python?", "Using curly braces"),
    ("What is the keyword to define a generator in Python?", "yield"),
    ("What is the output of: print(4 + 5)?", "9"),
    ("How do you create a list comprehension in Python?", "Using square brackets"),
    ("What is the method to check if a string starts with a specific substring?", "startswith"),
    ("What is the output of: print(7 % 3)?", "1"),
    ("How do you create a set comprehension in Python?", "Using curly braces"),
    ("What is the keyword to define a class in Python?", "class"),
    ("What is the method to check if a string ends with a specific substring?", "endswith"),
    ("What is the output of: print(9 // 2)?", "4"),
    ("How do you create a tuple comprehension in Python?", "Using parentheses"),
    ("What is the keyword to import a specific function from a module in Python?", "from"),
    ("What is the method to replace a substring in a string?", "replace"),
    ("What is the output of: print(8 / 4)?", "2.0"),
    ("How do you create a nested list in Python?", "Using square brackets inside square brackets"),
    ("What is the keyword to define an asynchronous function in Python?", "async"),
    ("What is the method to split a string into a list?", "split"),
    ("What is the output of: print(6 * 7)?", "42"),
    ("How do you create a multi-line string in Python?", "Using triple quotes"),
    ("What is the keyword to define a coroutine in Python?", "await"),
    ("What is the method to join a list of strings into a single string?", "join"),
    ("What is the output of: print(5 - 3)?", "2"),
    ("How do you create a dictionary comprehension in Python?", "Using curly braces"),
    ("What is the keyword to define a static method in Python?", "staticmethod"),
    ("What is the method to find the index of a substring in a string?", "find"),
    ("What is the output of: print(3 + 4)?", "7"),
    ("How do you create a generator expression in Python?", "Using parentheses"),
    ("What is the keyword to define a class method in Python?", "classmethod"),
    ("What is the method to count the occurrences of a substring in a string?", "count"),
    ("What is the output of: print(2 ** 4)?", "16"),
    ("How do you create a lambda function in Python?", "Using the lambda keyword"),
    ("What is the keyword to define a property in Python?", "property"),
    ("What is the method to check if a string contains only digits?", "isdigit"),
    ("What is the output of: print(7 - 5)?", "2"),
    ("How do you create a list of lists in Python?", "Using square brackets inside square brackets"),
    ("What is the keyword to define a private method in Python?", "Using double underscores"),
    ("What is the method to check if a string contains only alphabets?", "isalpha"),
    ("What is the output of: print(6 / 3)?", "2.0"),
    ("How do you create a dictionary of dictionaries in Python?", "Using curly braces inside curly braces"),