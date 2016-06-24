'''
    type: algorithm
    theme: math
    sub-theme: calculate
    name: factorial
    author of code: Evgeny @missingdays Bovykin

'''

def factorial(n):
    if n == 1 or n == 0:
        return 1

    a = 1

    for i in range(1, n+1):
        a = a * i

    return a