
n = 10
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

    
n = 5
for i in range(1, n+1):
    for j in range(i):
        print(j, end=" ")
    print()
    
n = 5
for i in range(1, n+1):
    for j in range(1, 2*n):
        if j == n-i+1 or j == n+i-1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
