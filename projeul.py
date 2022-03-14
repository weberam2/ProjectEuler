def primelist(N):
    # We will find all primes in the range 1 to 120
    # is_prime[i] = 1 means that i is prime and is_prime[i] = 0 means that i is composite
    # Initially, we say all of them are prime
    is_prime = [1]*N
    # We know 0 and 1 are composites
    is_prime[0] = 0
    is_prime[1] = 0

    def sieve():
        """
        We cross out all composites from 2 to sqrt(N)
        """
        i = 2
        # This will loop from 2 to int(sqrt(x))
        while i*i <= N:
            # If we already crossed out this number, then continue
            if is_prime[i] == 0:
                i += 1
                continue

            j = 2*i
            while j < N:
                # Cross out this as it is composite
                is_prime[j] = 0
                # j is incremented by i, because we want to cover all multiples of i
                j += i

            i += 1

    sieve()
    primelist = []
    for i in range(1, N):
        if is_prime[i] == 1:
            primelist.append(i)
    return primelist
