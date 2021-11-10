def prime(n):
    n = int(input("Enter a number: "))
    number = False
    if n < 0:
        return "please insert a natural number"
    elif 0 <= n < 2:
        return "number is not prime"
    elif n == 2:
        return "number is prime"
    else:
        for i in range(2, n):
            if (n % i) == 0:
                number = True
                break
    if number:
        return "number is not prime"
    else:
        return "number is prime"


print(prime(9))