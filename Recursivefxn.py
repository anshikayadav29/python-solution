# Recursive function to check if a string is palindrome

def is_palindrome(s):
    # Base case
    if len(s) <= 1:
        return True
    # Recursive case
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Taking input
text = input("Enter a string: ").lower()

if is_palindrome(text):
    print("Yes! It's a palindrome.")
else:
    print("Nope, not a palindrome.")
