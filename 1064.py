positivos = 0;
mP = [];

for i in range(6):
    x = float(input());
    if x>0:
        positivos+=1;
        
        mP.append(x);
        total = sum(mP)
        media = total/(len(mP));

print(f"{positivos:.0f} valores positivos");
print(f"{media:.1f}");
