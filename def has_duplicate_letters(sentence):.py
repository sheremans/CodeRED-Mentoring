def has_duplicate_letters(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Iterate through each word
    for word in words:
        # Check for duplicate letters using a set
        letter_set = set()
        for letter in word:
            # If a letter is already in the set, it's a duplicate
            if letter in letter_set:
                return True
            letter_set.add(letter)

    # No duplicates found in any word
    return False

# Example usage:
sentence = "Always forgive your enemies; nothing annooys them so much."
result = has_duplicate_letters(sentence)

if result:
    print("The sentence contains words with duplicate letters.")
else:
    print("No words in the sentence have duplicate letters.")