# Prime Number Checker in Python

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# User input
n = int(input("Enter a number: "))

if is_prime(n):
    print(f"{n} is a Prime Number ✅")
else:
    print(f"{n} is NOT a Prime Number ❌")
