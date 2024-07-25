# # # Debug and fix errors in Python code.


# Original buggy code:

def divide(a, b):
    return a / b

print(divide(5, 0))



# Fixed code:
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is undefined"

print(divide(5, 0))
