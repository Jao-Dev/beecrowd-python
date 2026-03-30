t = int(input());
n = [];
valor = 0;

for i in range(1000):
    n.append(valor);
    valor+=1;
    if valor==t:
        valor = 0;

for i in range(1000):
    print(f"N[{i}] = {n[i]}");