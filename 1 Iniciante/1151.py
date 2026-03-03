x = int(input())
y = 1;
fibo = [0, 1];
for i in range(2, x):
    fibo.append(fibo[i-1] + fibo[i-2])

print(" ".join(map(str, fibo[:x])))