def factorial(num, show=False):
    """
        -> Calculates the factorial of a number
        :param num: The number that will be calculated
        :param show: (optional) Show or not the full operation
        :return: returns the factorial value of that number
    """
    finalResult = 1
    for i in range(num, 0, -1):
        if(show):
            print(i, end=' x ' if i > 1 else ' = ')
        finalResult *= i
    return finalResult

#Main
help(factorial)
print(factorial(5, True))
print(factorial(4))
print(factorial(2, False))