#Hollow square 1
n = 9
for i in range(n):
    for j in range(n):
        if i == 0 or i == 8 or j == 0 or j == 8:#n-1
            print(j , end="  ")
        else:
            print("  ", end="  ")
    print()
print("----------------------------------------------------")
#hollow square 2
n = 10

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:#n=9
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("----------------------------------------------------")
#3.
#hollow square 3
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == 4 or j == 0 or j == 4: #n-1
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("----------------------------------------------------")
#Square of i
n=5
for i in range(n):
    for j in range(n):
        print(i, end=" ")#continue 0000 1111 2222 3333
    print()
print("----------------------------------------------------")
#Square of j
n=6
for i in range(n):
    for j in range(n):
        print(j,end=" ")#012345
    print()
print("----------------------------------------------------")    
#Plus pattern
n = 7
for i in range(n):
    for j in range(n):
        if i == 3 or j == 3:
            print(j, end=" ")
        else:
            print(" ",  end=" ")
    print()
print("----------------------------------------------------")
#plus pattern in *
n = 7
for i in range(n):
    for j in range(n):
        if i == 3 or j == 3:
            print("*", end=" ")
        else:
            print(" ",  end=" ")
    print()
print("----------------------------------------------------")
#plus pattern in PYTHON
n = 11
for i in range(n):
    for j in range(n):
        if i == 6 or j == 6:
            print(j, end=" ")
        else:
            print(" ",  end=" ")
    print()
print("----------------------------------------------------")
# 5.
n = 5
for i in range(n):
    for j in range(n):
        if i == 2 or j == 2:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()
print("----------------------------------------------------")
#CROSS PATTERN

n=8
for i in range(n):
    for j in range(n):
      if i == j or i+j == 6:
          print("*", end=" ")
      else:
          print(" ", end=" ")
    print()
print("----------------------------------------------------")
#number in Cross pattern

n = 8
for i in range(n):
    for j in range(n):
      if i == j or i+j == 6:
          print(j, end=" ")
      else:
          print(" ", end=" ")
    print()
print("----------------------------------------------------")
#python in cross pattern

s="PYTHONN"
for i in range(n):
    for j in range(n):
      if i == j or i+j == 6:
          print(s [i] , end=" ")
      else:
          print(" ", end=" ")
    print()
print("----------------------------------------------------")
#python in APPLE

s = "APPLE"
n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == 4:
            print(s[i], end=" ")
        else:
            print(" ", end=" ")
    print()
print("----------------------------------------------------")


                
