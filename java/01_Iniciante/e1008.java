import java.util.Scanner;

public class e1008 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numero = scanner.nextInt();
        int horas = scanner.nextInt();
        double valor = scanner.nextDouble();

        double salario = valor*horas;

        System.out.printf("NUMBER = %d\n", numero);
        System.out.printf("SALARY = U$ %.2f\n", salario);

        scanner.close();
    }
}
