def factorial(number):
  if number <= 0:
    return 0
  if number == 1:
    return 1
     #simple multiplication of numbers to get the factorial of a number
  return number*factorial(number-1)
def fibiconi(number):
  if number <= 0: # resolving problem of 0 and negative fibonacci numbers
    return 0
  if number == 1 or number == 2:   # resolving problem of 1st and 2nd fibonacci numbers
    return 1

  return fibiconi(number-1) + fibiconi(number-2)


print(fibiconi(10))
print(factorial(5))