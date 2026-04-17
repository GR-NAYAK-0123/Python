
# Here I have to write write a program to find the prime numbers with in a range

def check_prime(num):
    if num == 1:
        return False
    for i in range(2,(num//2)+1):
        if num % i == 0:
            return False
    return True

def prime_numbers(start, end):
    result = []
    for i in range(start,end+1):
        if check_prime(i):
            result.append(i)
    return result

print(prime_numbers(1, 55))