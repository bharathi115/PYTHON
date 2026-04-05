n = 5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
print("------------------------")
n = 8
for i in range(n):
    for j in range(n):
        if i == 0 or i == 7 or j == 0 or j == 7:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("------------------------") 
n = 5
for i in range(n):
    num = 1
    for j in range(i+1):
        print(j, end=" ")
        num = num * (i-j) // (j+1)
    print()

print("------------------------")
n = 6
for i in range(1,n+1):
    for j in range(i):
        print(i, end=" ")
    print()

print("------------------------")
n = 6
for i in range(n,0,-1):
    for j in range(i):
        print(i, end=" ")
    print()
print("------------------------")
n = 9
for i in range(n):
    for j in range(n):
        if i==4 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("------------------------")
n = 9
for i in range(n):
    for j in range(n):
        if i==j or j+i == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
                      
print("------------------------")
n = 6
for i in range(n,0,-1):
    for j in range(i):
        print("#", end=" ")
    print()
