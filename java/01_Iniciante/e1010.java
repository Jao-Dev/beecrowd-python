import java.util.Scanner;

public class e1010 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int codP1 = sc.nextInt();
        int numP1 = sc.nextInt();
        double uniP1 = sc.nextDouble();

        int codP2 = sc.nextInt();
        int numP2 = sc.nextInt();
        double uniP2 = sc.nextDouble();

        double resultado = (numP1*uniP1)+(numP2*uniP2);

        System.out.printf("VALOR A PAGAR: R$ %.2f\n", resultado);

        sc.close();
    }
}
