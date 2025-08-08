import math
from functools import reduce

def lcm(a, b):
    return a * b // math.gcd(a, b)

p = int(input("Введіть кількість чисел: "))
numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

result = reduce(lcm, numbers)
print(result)

input()  
