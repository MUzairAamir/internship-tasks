def factorial(number):
  if number <= 0:
    return 0
  if number == 1:
    return 1

  return number*factorial(number-1)
def fibiconi(number):
  if number <= 0:
    return 0
  if number == 1 or number == 2:
    return 1

  return fibiconi(number-1) + fibiconi(number-2)