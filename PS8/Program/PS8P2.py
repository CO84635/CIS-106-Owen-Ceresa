a = 1
b = 1

print("The first 20 numbers of Fibonacci sequence is: ")
print(a)


for x in range (20):
    a, b = b, a + b
    print(a)
