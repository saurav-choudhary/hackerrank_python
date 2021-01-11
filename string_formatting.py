def print_formatted(number):
    temp = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(str(i).rjust(temp, ' '), end=' ')
        print(oct(i)[2:].rjust(temp, ' '), end=' ')
        print(hex(i)[2:].rjust(temp, ' ').upper(), end=' ')
        print(bin(i)[2:].rjust(temp, ' '), end=' ')
        print('')


n = 0
while n not in range(1, 100):
    n = int(input())
print(print_formatted(n))
