x, y, z = map(int, input().split());

maiorXY = (x+y+abs(x-y))/2;
maior = (maiorXY+z+abs(maiorXY-z))/2;
print(f'{maior:.0f} eh o maior');