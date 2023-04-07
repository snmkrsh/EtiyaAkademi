
x = 1
y = 1
fib= [x,y]

for i in range(20):
    z = x + y
    x = y
    y = z
    fib.append(z)
print(fib)


