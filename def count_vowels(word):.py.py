def count_vowels(word):
    # Convert the word to lowercase for case-insensitive counting
    word_lower = word.lower()

    # Define the set of vowels
    vowels = set("aeiou")

    # Count the number of vowels in the word
    vowel_count = sum(1 for char in word_lower if char in vowels)

    return vowel_count


 word = "Mexico"
 vowel_count = count_vowels(word)

 print(f"The word '{word}' has {vowel_count} vowels.")