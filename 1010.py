codP1, numP1, valUnP1 = map(float, input().split());
codP2, numP2, valUnP2 = map(float, input().split());

p1 = numP1*valUnP1;
p2 = numP2*valUnP2;
vap = p1+p2;

print(f'VALOR A PAGAR: R$ {vap:.2f}');
