a = int(input("Введите число: "))
def factorial(n):
    B = 1
    while n >= 1:
        B = B * n
        n = n - 1
    return B
A = factorial(a)
print(A)
