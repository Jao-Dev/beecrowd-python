x = int(input());

ano = x//365;
x = x%365;
mes = x//30;
dia = x%30;

print(f'{ano} ano(s)');
print(f'{mes} mes(es)');
print(f'{dia} dia(s)');