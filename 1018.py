x = int(input());

d100 = x//100;
d50 = (x%100)//50;
d20 = ((x%100)%50)//20;
d10 = (((x%100)%50)%20)//10;
d5 = ((((x%100)%50)%20)%10)//5;
d2 = (((((x%100)%50)%20)%10)%5)//2;
d1 = ((((((x%100)%50)%20)%10)%5)%2)//1;

print(x);
print(f'{d100} nota(s) de R$ 100,00');
print(f'{d50} nota(s) de R$ 50,00');
print(f'{d20} nota(s) de R$ 20,00');
print(f'{d10} nota(s) de R$ 10,00');
print(f'{d5} nota(s) de R$ 5,00');
print(f'{d2} nota(s) de R$ 2,00');
print(f'{d1} nota(s) de R$ 1,00');

'''
x = int(input())
print(x) for nota in [100, 50, 20, 10, 5, 2, 1]:
    qtd = x // nota
    print(f"{qtd} nota(s) de R$ {nota},00")
    x %= nota
'''