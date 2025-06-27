def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

num = 7
if is_even(num):
    print(num, "is Even")
else:
    print(num, "is Odd")