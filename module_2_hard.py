n = input('Введите число n от 3 до 20, n: ')
n = int(n)

password = []


for i in range(1, n - 1):
    for j in range(i + 1,  n):

        if n % (i + j) == 0:
            password.append(i)
            password.append(j)

print(n, ':', password)
