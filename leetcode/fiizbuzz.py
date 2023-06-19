def fizzBuzz(n):
    # Write your code here
    for i in range(1, n):
        if n % 3 == 0 and n % 5 == 0:
            return("FizzBuzz")
        elif n % 3 == 0:
            return("Fizz")
        elif n % 5 == 0:
            return("Buzz")

    return(n)

fizzBuzz(15)