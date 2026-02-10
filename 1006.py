pesoX = 2;
pesoY = 3;
pesoZ = 5;
pesoTotal = pesoX + pesoY + pesoZ;

x = (float(input()))*pesoX;
y = (float(input()))*pesoY;
z = (float(input()))*pesoZ;

MEDIA = (x+y+z)/pesoTotal;
print(f'MEDIA = {MEDIA:.1f}');