# Palindrome Checker in Python

def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word: ")
if is_palindrome(word):
    print(f"✅ '{word}' is a Palindrome")
else:
    print(f"❌ '{word}' is not a Palindrome")
