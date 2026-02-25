x = float(input());

if x>=0 and x<=400.00:
    percentual = 0.15
    reajuste = x*percentual;
    salario = x+reajuste;
    print(f"Novo salario: {salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual*100:.0f} %")

elif x>=400.01 and x<=800.00:
    percentual = 0.12
    reajuste = x*percentual;
    salario = x+reajuste;
    print(f"Novo salario: {salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual*100:.0f} %")

elif x>=800.01 and x<=1200.00:
    percentual = 0.1
    reajuste = x*percentual;
    salario = x+reajuste;
    print(f"Novo salario: {salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual*100:.0f} %")

elif x>=1200.01 and x<=2000.00:
    percentual = 0.07
    reajuste = x*percentual;
    salario = x+reajuste;
    print(f"Novo salario: {salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual*100:.0f} %")

elif x>2000:
    percentual = 0.04
    reajuste = x*percentual;
    salario = x+reajuste;
    print(f"Novo salario: {salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual*100:.0f} %")

