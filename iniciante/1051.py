x = float(input())

if x <= 2000.00:
    print("Isento")
elif x <= 3000.00:
    imposto = (x - 2000.00) * 0.08
    print(f"R$ {imposto:.2f}")
elif x <= 4500.00:
    imposto = (1000.00 * 0.08) + (x - 3000.00) * 0.18
    print(f"R$ {imposto:.2f}")
else:
    imposto = (1000.00 * 0.08) + (1500.00 * 0.18) + (x - 4500.00) * 0.28
    print(f"R$ {imposto:.2f}")
