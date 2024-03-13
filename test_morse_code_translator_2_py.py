def test_text_to_morse(input_text):
    morse_code = ''
    for char in input_text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += char  # Keep non-alphanumeric characters as is
    return morse_code.strip()

# Only take input in the main function, not in global scope
def test_main():
    user_input = input("provide the proof: ")
    morse_result = text_to_morse(user_input)
    print("Morse Code:", morse_result)

# Check if the script is run directly
if __name__ == "__main__":
    main()