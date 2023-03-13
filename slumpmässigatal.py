import random 
t = list()
sum = 0 
for i in range(1, 100):
    x = random.randint(1, 1000)
    sum += x 
    t.append(x)
print(f'Minsta tal: {}')
