pesoX = 3.5;
pesoY = 7.5;
pesoTotal = pesoX + pesoY;

x = (float(input()))*pesoX;
y = (float(input()))*pesoY;

MEDIA = (x+y)/pesoTotal;
print(f'MEDIA = {MEDIA:.5f}');