# TABIND-Scrabble-Project
Develop a program that finds and alphabetically lists all valid Scrabble words that can be formed using the letters in “tabind” only once.

## How it works

The program reads every word from `scrabble_dictionary.txt`.

For each word, it checks:

- the word is not longer than `tabind`
- every letter in the word is inside `tabind`
- no letter is used more times than it appears in `tabind`

Then it prints all valid words in alphabetical order and saves them in `valid_words.txt`.

The Scrabble dictionary file used in this project has 178,690 words.

The program found 49 valid words that can be made from `tabind`.

## How to run

The Scrabble dictionary file is already in this folder:

```text
scrabble_dictionary.txt
```

Run the program with:

```bash
python3 main.py
```

After running the program, the results will be saved in:

```text
valid_words.txt
```
