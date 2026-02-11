x = int(input());

hr = x//3600;

x = x%3600;

mn = x//60;
sc = x%60;

print(f'{hr:.0f}:{mn:.0f}:{sc:.0f}');