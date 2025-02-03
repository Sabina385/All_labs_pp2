class PrimeFilter:
    def filter_primes(self, numbers):
        return list(filter(lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)), numbers))

numbers = list(map(int, input("Enter a numbers: ").split()))
print(PrimeFilter().filter_primes(numbers))