def get_random_code():
  import random
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  operators = ['+', '-', '*', '/']
  variables = ['x', 'y', 'z']
  
  code = ''
  for i in range(10):
    num = random.choice(numbers)
    op = random.choice(operators)
    var = random.choice(variables)
    
    if op == '+':
      code += f'{num} + {var}'
    elif op == '-':
      code += f'{num} - {var}'
    elif op == '*':
      code += f'{num} * {var}'
    else:
      code += f'{num} / {var}'
    
  return code
