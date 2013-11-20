import random

operators = ['+', '-', '*']
print('Range:')
i = input() 
m, M = map(int, i.split(" ")) # Integers from m to M
generateNew = True
while True:
    if generateNew:
        a, b, c, d = random.randint(m, M), random.randint(m, M), random.randint(m, M), random.randint(m, M)
        o1, o2, o3 = int(len(operators)*random.random()), int(len(operators)*random.random()), int(len(operators)*random.random())
        s = '{} {} {} {} {} {} {}'.format(a, operators[o1], b, operators[o2], c, operators[o3], d)
        generateNew = False
        print(s)
    
    i = input()
    if i == 'q': break
    
    i = int(i)
    if (eval(s) == i):
        print('Correct!')
        generateNew = True
    else:
        print('Incorrect...')
