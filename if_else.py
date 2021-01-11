# Ik that I made the code unnecessarily long

n = 0

while n not in range(1, 101):
    n = int(input().strip())


def is_even(number):
    if number % 2 == 0:
        return True
    return False


if not is_even(n):
    print('Weird')

if is_even(n):
    if 2 <= n <= 5:
        print('Not Weird')
    elif 6 <= n <= 20:
        print('Weird')
    elif n >= 20:
        print('Not Weird')

# # I found a better and compact solution in the discussions section.
# check = {True: 'Not Weird', False: 'Weird'}
# print(check[n % 2 == 0 and (n in range(2, 6) or n > 200)])
