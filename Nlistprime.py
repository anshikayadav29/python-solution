# primes_up_to_n.py
def primes_up_to(n):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= n:
        if sieve[p]:
            for multiple in range(p*p, n+1, p):
                sieve[multiple] = False
        p += 1
    return [i for i, is_prime in enumerate(sieve) if is_prime]

if __name__ == "__main__":
    n = int(input("n daalo (list primes up to n): "))
    primes = primes_up_to(n)
    print(f"Primes up to {n}:")
    print(primes)
