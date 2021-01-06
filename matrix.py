import random,os
os.system('clear')
a=[chr(i)for i in range(30,300)]
for i in range(100):
    a.append('')
while True:
    b=[]
    for c in range(10):
        b.append(random.choice(a))
    for n in b:
        print('\033[1;32m'+n,end='')

