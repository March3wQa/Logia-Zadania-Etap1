def o6(max):
    try:
        if max<12 or max>10000:
            raise ValueError('Błędna liczba. Akceptowane liczby to od 12 do 10000.')
    except ValueError as err:
        return err
    else:
        ### GENERATOR LICZB PIERWSZYCH ###
        primes = [2, 3]
        n = 4
        for _ in range(max):
            tries = 0
            for i in range(len(primes)):
                if n%primes[i] != 0:
                    tries += 1
            if tries == len(primes):
                primes.append(n)
            n += 1
        ##################################

        ### SPRAWDZANIE PARY ###
        while primes[len(primes)-1] > max:
            del primes[len(primes)-1]
        else:
            try:
                for k in primes:
                    c1 = primes[len(primes)-k]
                    c2 = primes[len(primes)-(k+1)]
                    if c1-6 == c2:
                        return c1
            except IndexError:
                for k in primes:
                    c1 = primes[len(primes)-1]
                    c2 = primes[len(primes)-(k+1)]
                    if c1-6 == c2:
                        return c1
        ########################