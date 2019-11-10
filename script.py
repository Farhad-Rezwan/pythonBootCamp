# read a list of integers form user input
# Find all pairs of numbers in the list whose product is even and whose sum is odd

print ("Enter list of numbers delimited by space")

x = list(map(int, input().split()))

ans = []
i = 0
while i < len(x):    
    j = 0
    while j < len(x):
        if (i <= j):
            if (x[i] * x[j]) % 2 == 0:
                if (x[i] + x[j]) % 2 != 0:
                    abc = list((x[i], x[j]))
                    ans.append(abc)
            
        
        j += 1
    i += 1
print(ans)