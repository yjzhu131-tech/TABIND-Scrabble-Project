# TABIND-Scrabble-Project

# The objective of this project is to develop a program 
# that takes the letter combination “tabind” only once and 
# creates an alphabetical list of all the words, from a Scrabble dictionary 
# that can be found with those letters. 

# These are the letters we can use.
# Each letter can only be used as many times as it appears here.
letters = "tabind"

# This is the dictionary file that the program will read.
dictionary_file = "scrabble_dictionary.txt"

# This is the file where the final answer will be saved.
output_file = "valid_words.txt"


def can_make_word(word):
    # An empty word should not be counted.
    if len(word) == 0:
        return False

    # A word cannot be longer than the letters we have.
    if len(word) > len(letters):
        return False

    # Check each letter in the word.
    for letter in word:
        # If the letter is not in "tabind", this word is not valid.
        if letter not in letters:
            return False

        # If the word uses this letter too many times, it is not valid.
        if word.count(letter) > letters.count(letter):
            return False

    # If none of the checks failed, the word is valid.
    return True


# This list will store all valid words we find.
valid_words = []

try:
    # Open the Scrabble dictionary file.
    file = open(dictionary_file, "r")

    # Read the dictionary one line at a time.
    for line in file:
        # Remove spaces/new lines and make the word lowercase.
        word = line.strip().lower()

        # Check if the word can be made from "tabind".
        if can_make_word(word):
            # Add the word only if it is not already in the list.
            if word not in valid_words:
                valid_words.append(word)

    # Close the dictionary file after reading it.
    file.close()

    # Sort the words alphabetically.
    valid_words.sort()

    # Open the output file so we can save the results.
    result_file = open(output_file, "w")

    # Print each valid word and write it to the output file.
    for word in valid_words:
        print(word)
        result_file.write(word + "\n")

    # Close the output file after writing all results.
    result_file.close()

    print("")
    print("Results saved to " + output_file)

except FileNotFoundError:
    print("Could not find " + dictionary_file)
    print("Please put the Scrabble dictionary file in this folder.")
