x = int(input());

for i in range(x):
    a, b, c = map(float, input().split());
    aP=2*a;
    bP=3*b;
    cP=5*c;

    media = (aP+bP+cP)/10;
    print(f"{media:.1f}");