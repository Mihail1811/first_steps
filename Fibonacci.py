def check_for_prime(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def fibonacci(num: int) -> int:
    if num in (0, 1):
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

list_fib = []

with open('in_nums.txt', 'r') as r_file:
    for line in r_file:
        if check_for_prime(int(line)):
            fib_last_digit = fibonacci(int(line) % 10)
            list_fib.append(fib_last_digit)

with open('out_nums.txt', 'w') as wr_file:
    for num_fib in list_fib:
        wr_file.write(str(num_fib) + '\n')