def output(a, b):
  x = ''
  for i in range(a, b):
    if i%3==0 and i%5==0:
      x = x + 'FizzBuzz'
    elif i%3==0:
      x = x + 'Fizz'
    elif i%5==0:
      x = x + 'Buzz'
    else:
      x = x + str(i)
    x = x + '\n'
  return x
    