def print_matrix(n):
    for i in range(n):
        for j in range(n):
            print("*",end=' ')
        print()

# print_matrix(5)

def increase_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()

# increase_pattern(5)

def decrease_pattern(n):
    for i in range(n):
        for j in range(i,n):
            print('*',end=' ')
        print()
# decrease_pattern(5)

n=5
for i in range(n):
        for j in range(i,n):
            print(' ',end=' ') #decreasing_space
        for j in range(i+1):
            print('*',end=' ') # followed by two increase_pattern
        for j in range(i):
            print('*',end=' ') #prints uphill n
        print()