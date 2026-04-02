import java.util.Scanner;

public class e1066 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int pares = 0;
        int impares = 0;
        int positivos = 0;
        int negativos = 0; 

        for(int i=0; i<5; i++){

            int x = sc.nextInt();
            if(x%2==0){pares+=1;}
            if(x%2!=0){impares+=1;}
            if(x>0){positivos+=1;}
            if(x<0){negativos+=1;}
        }

        System.out.printf("%d valor(es) par(es)\n", pares);
        System.out.printf("%d valor(es) impar(es)\n", impares);
        System.out.printf("%d valor(es) positivo(s)\n", positivos);
        System.out.printf("%d valor(es) negativo(s)\n", negativos);

        sc.close();
    }
}
