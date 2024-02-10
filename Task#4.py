#Fibonacci series
print("####Fibonacci Series####")
n = int(input("Please Enter a Number: "))
n0 = 0
n1 = 1
i = 0
print(n0)
print(n1)
for i in range(n):
    a = n0 + n1
    print(a)
    n0 = n1
    n1 = a