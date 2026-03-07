x=int(input());

for i in range(x):
    y,z=input().split();

    a = len(y)-len(z);
    b = y[a:len(y)];

    if y==z or z==b:print("encaixa");
    else:print("nao encaixa");