x = int(input());

cobaias = [];
coelhos = 0;
ratos = 0;
sapos = 0;

for i in range(x):
    y, z = input().split();
    y = int(y);
    cobaias.append(y);
    
    if z=="C":
        coelhos = coelhos+y;
    elif z=="R":
        ratos = ratos+y;
    elif z=="S":
        sapos = sapos+y;

ttCobaias = sum(cobaias)
print(f"Total: {ttCobaias} cobaias");
print(f"Total de coelhos: {coelhos}");
print(f"Total de ratos: {ratos}");
print(f"Total de sapos: {sapos}");

print(f"Percentual de coelhos: {coelhos/ttCobaias*100:.2f} %");
print(f"Percentual de ratos: {ratos/ttCobaias*100:.2f} %");
print(f"Percentual de sapos: {sapos/ttCobaias*100:.2f} %");
