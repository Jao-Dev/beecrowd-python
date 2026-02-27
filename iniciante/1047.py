hI, mI, hF, mF = map(int, input().split());

tInicial = (hI*60)+mI;
tFinal = (hF*60)+mF;

dTotal = tFinal - tInicial;
if dTotal <=0:
    dTotal += 24*60;

horas = dTotal//60;
minutos = dTotal%60;

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)");