import java.util.Scanner;

public class e1007 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        int d = scanner.nextInt();

        int dif = (a*b-c*d);

        System.out.printf("DIFERENCA = %d\n", dif);

        scanner.close();
    }
}
