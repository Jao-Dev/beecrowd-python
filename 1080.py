valores = [];

for i in range(100):
    x = int(input());
    valores.append(x);

maior = max(valores);
posicao = valores.index(maior)+1;

print(maior);
print(posicao);
