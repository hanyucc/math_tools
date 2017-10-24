def prime_sieve(max_num):
    is_prime = [True for i in range(max_num + 1)]
    primes = list()

    for i in range(2, max_num + 1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if p * i > max_num:
                break
            is_prime[p * i] = False
            if not i % p:
                break

    return primes


def main():
    max_num = int(input('maximum number: '))
    print(prime_sieve(max_num))


if __name__ == '__main__':
    main()
