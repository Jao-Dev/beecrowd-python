v = [];
while len(v)<2:
    x = float(input());
    if x>=0 and x<=10:
        v.append(x);
    else:
        print("nota invalida");
media = (v[0]+v[1])/2;
print(f"media = {media}");