x, y = map(int, input().split());

if x>y:
    horas = (24-x)+y;
    print(f"O JOGO DUROU {horas} HORA(S)");
elif y>x:
    horas = (y-x);
    print(f"O JOGO DUROU {horas} HORA(S)");
else:
    print(f"O JOGO DUROU 24 HORA(S)");