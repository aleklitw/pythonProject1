def prime(n):
    for i in range(2, n):
        if n % i == 0:
            print("not a prime")
        break
    else:
        print("is a prime")


print(prime(10))
