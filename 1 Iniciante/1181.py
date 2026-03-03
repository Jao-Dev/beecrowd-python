m = [];
x = int(input());
y = input();

for i in range(12):
    linha = [];
    for j in range(12):
        linha.append(float(input()));
    m.append(linha);
linhaEscolhida = m[x];

if y=="S":
    print(f"{sum(linhaEscolhida):.1f}");
elif y=="M":
    print(f"{sum(linhaEscolhida)/12:.1f}");