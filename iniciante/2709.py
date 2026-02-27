"""As Moedas de Robbie"""

import math;

qntdMoedas = int(input());
moedas = [];
moedasSelecionadas = []

for i in range(qntdMoedas):
    x = int(input());
    moedas.append(x);

numSaltos = int(input());

for i in range(qntdMoedas-1, -1, -numSaltos):
    moedasSelecionadas.append(moedas[i]);

soma = sum(moedasSelecionadas);

"""Essa função de verificação peguei online"""
def primo(soma):
    if soma <= 1:
        return False
    if soma == 2:
        return True
    if soma % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(soma)) + 1, 2):
        if soma % i == 0:
            return False
    return True
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""

if primo(soma):
    print("You’re a coastal aircraft, Robbie, a large silver aircraft.");
else:
    print("Bad boy! I’ll hit you.");