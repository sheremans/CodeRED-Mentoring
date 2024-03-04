import re

def count_words(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the contents of the file
            content = file.read()

            # Count the words using regular expression
            words = re.findall(r'\b\w+\b', content)
            word_count = len(words)

            return word_count
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return -1
    except Exception as e:
        print(f"Error: {e}")
        return -1


file_name = "Assignment 2 Codered txt file.txt"
desktop_path = "/Users/anastasiasheremet/Desktop/"
file_path = desktop_path + file_name

word_count = count_words(file_path)

if word_count != -1:
    print(f"The number of words in the file '{file_name}' is: {word_count}")
