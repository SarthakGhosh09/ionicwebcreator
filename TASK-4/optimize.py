#  Optimize code for better performance where possible.

#  Original less efficient code:

numbers = [x for x in range(1, 1000001)]
squares = []
for number in numbers:
    squares.append(number ** 2)

# Optimized code:


numbers = range(1, 1000001)
squares = [x**2 for x in numbers]
