# Check if it's a Prime number

def prime_checker(number):
    for i in range(2, number):  # It will not be a Prime number if you can divide it by 1, 2, or 4.
        if number % i == 0:
            print("It's not a prime number.")
            break

        if i + 1 == number:
            print("It's a prime number.")


n = int(input("Provide Number: "))  # Check this number
prime_checker(number=n)
