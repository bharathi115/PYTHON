
 #ASCII value in SQuare   
n = 6
c = 65  # ASCII 
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == 4 or j == 4:
            print(j, end=" ")
        else:
            print(chr(c), end=" ")
            c += 1
    print()
