
# map() — Har item ko change karo
# Example: 

numbers = [1, 2,3,4,5,6]
def square(n):
    return n*n

result = map(square, numbers)
print(list(result))

# filter() — Condition ke basis par select karo
# Example: 

numbers = [1, 2,3,4,5,6]
def is_even(n):
    return n % 2==0
result = filter(is_even,numbers)

print(list(result))

# Lambda version:

numbers = [1, 2,3,4,5,6]
result = list(filter(lambda n:n %2 ==0, numbers))
print(result)

# reduce() — Sab items ko combine karke ek result banao
# Example:
from functools import reduce
numbers = [1,2,3,4,5,6]
result = reduce(lambda a, b,:a*b, numbers)
print(result)

