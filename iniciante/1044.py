x, y = map(int, input().split());

def mult(x, y):
    return (y%x==0) or (x%y==0);

if mult(x, y):
    print("Sao Multiplos");
else:
    print("Nao sao Multiplos");
