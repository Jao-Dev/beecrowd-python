"""Magic and Sword

obs.: Se eu não tivesse faltado as aulas de matemática seria mais fácil (y).
"""

import math;

t = int(input());


for i in range(t):

    """Personagem"""
    w, h, x0, y0 = map(int, input().split());
    x1 = x0+w;
    y1 = y0+h; 

    """Magia"""
    magia, nivel, cx, cy = input().split();
    nivel = int(nivel);
    cx = int(cx);
    cy = int(cy);


    if magia=="fire":
        dano = 200;
        raio = [20, 30, 50][nivel-1];
    elif magia=="water":
        dano = 300;
        raio = [10, 25, 40][nivel-1];
    elif magia=="earth":
        dano = 400;
        raio = [25, 55, 70][nivel-1];
    elif magia=="air":
        dano = 100;
        raio = [18, 38, 60][nivel-1];

    
   
        """Raio da magia"""
    px = min(max(cx, x0), x1);
    py = min(max(cy, y0), y1);
    dist = math.sqrt((cx-px)**2 + (cy-py)**2);
               
    if dist <= raio:
        print(dano);
    else:
        print(0)

